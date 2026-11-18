"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Mặc định dưới đây cho qua tất cả (= mốc base).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    # Resolve validity by dates, rather than the search index's active flag.
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không tìm được chính sách có hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()
    order = ctx.tools.lookup_order(action.get("order_id") or action.get("payload", {}).get("order_id"))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not policy or order.get("customer_id") != ctx.ticket.get("customer_id"):
        return Verdict.escalate("không xác minh được đơn, chủ đơn hoặc chính sách")
    parcels = order.get("parcels") or []
    if not parcels or (ctx.ticket.get("parcel_id") and not any(
            p["parcel_id"] == ctx.ticket["parcel_id"] for p in parcels)):
        return Verdict.escalate("không xác minh được kiện thuộc yêu cầu")
    try:
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        delay = H.db_delay_days(parcel, ctx.as_of)
        expected = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
    except (KeyError, TypeError, ValueError):
        return Verdict.escalate("tracking hoặc chính sách thiếu dữ liệu hợp lệ")

    if tool == "issue_refund":
        # Never use model claims as authorization to move money.
        amount = action.get("amount_vnd")
        if (type(amount) is not int or amount <= 0 or amount != expected
                or action.get("payer", "LOGIX") != "LOGIX"
                or action.get("basis", "policy") != "policy"):
            return Verdict.escalate("khoản hoàn không khớp quyền lợi từ tracking và policy")
        if ctx.tools.ledger_rows(order_id=order["order_id"]):
            return Verdict.deny("đơn đã có khoản hoàn trong sổ, không ghi trùng")
        approval_id = action.get("approval_id")
        if amount > policy["auto_limit_vnd"] or approval_id:
            approvals = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
            valid = any(a.get("status") == "valid"
                        and a.get("order_id") == order["order_id"]
                        and a.get("customer_id") == ctx.ticket.get("customer_id")
                        and a.get("ticket_id") == ctx.ticket.get("ticket_id")
                        and bool(a.get("approver_id"))
                        and (not ctx.gates.get("operations", {}).get("approver_id")
                             or a.get("approver_id") == ctx.gates["operations"]["approver_id"])
                        and a.get("expires_at", "") >= ctx.as_of
                        and a.get("max_vnd", 0) >= amount
                        and not ctx.tools.ledger_rows(approval_id=a.get("approval_id"))
                        for a in approvals)
            if not valid:
                return Verdict.escalate("chưa có phê duyệt hợp lệ khớp khoản hoàn")
        return Verdict.allow()

    if tool == "file_carrier_fault":
        if (not H.carrier_at_fault(policy, parcel, delay)
                or action.get("parcel_id") != parcel["parcel_id"]
                or action.get("carrier_id") != parcel["carrier_id"]
                or action.get("driver_id") != parcel.get("driver_id")
                or action.get("delay_days") != delay):
            return Verdict.deny("lỗi hãng không khớp kiện, tracking hoặc policy hiệu lực")
        if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
            return Verdict.deny("kiện đã được ghi lỗi, không ghi trùng")
        return Verdict.allow()

    # Build a minimal payload from authoritative facts; never forward free text
    # or nested recipient contacts supplied by the model/customer.
    if action.get("carrier_id") != parcel["carrier_id"]:
        return Verdict.deny("hãng nhận thông báo không khớp kiện")
    facts = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
             "district": order.get("recipient", {}).get("district"), "delay_days": delay}
    blocked = set(ctx.gates.get("legal", {}).get("pii_fields_blocked_to_third_party") or [])
    payload = {k: v for k, v in facts.items()
               if k in policy.get("carrier_notice_fields", []) and k not in blocked and v is not None}
    return Verdict.modify("chỉ gửi dữ liệu tối thiểu được policy và legal cho phép", payload=payload)
