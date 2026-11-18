"""★ FILE ĐỘI SỬA (2/3): chỉ số theo dõi (monitor). Thêm ÍT NHẤT MỘT chỉ số bắt được sự cố của bàn.

Mỗi monitor nhận danh sách trial (KHÔNG có nhãn đúng/sai, giống production) và trả về một số.
Một trial = {"ticket_id", "seed", "day", "status", "amount_vnd", "ticket", "events", "ledger", "faults", "outbound",
             "arrive_min", "warehouse", "cost_vnd", "review_kind", "queue_wait_min", "queue_stuck"}
  "day"            một ngày vận hành giả lập: các ticket cùng "day" và cùng "seed" chạy nối nhau trên cùng một sổ cái
  "arrive_min"     phút ticket tới trong ca (0..480)          "warehouse"   kho của đơn
  "cost_vnd"       tiền LLM + nền tảng đã tốn cho ticket      "review_kind" None / "escalated" (trợ lý chuyển người) /
  "queue_wait_min" số phút chờ người duyệt (None nếu không vào hàng chờ)     "recheck" (nhân viên tự kiểm lại)
Chỉ số có thể là kỹ thuật (tỉ lệ model đè số trong ticket lên DB), vận hành (số ca cần người trong giờ đông nhất),
hay kinh doanh (tỉ lệ ticket trợ lý đọc xong vẫn phải chuyển người).

lab10.grade kiểm: monitor chạy không lỗi, và giá trị trên gói sự cố khác giá trị trên bộ nền,
tức là monitor "sáng đèn" khi sự cố xảy ra.
"""


def escalation_rate(trials):
    return sum(t["status"] == "escalated" for t in trials) / max(1, len(trials))


def multi_parcel_exposure_rate(trials):
    """Fraction of trials with multiple parcels; exposure, not a harm label."""
    def exposed(trial):
        return any((e.get("type") == "tracking" and len(e.get("parcels", [])) > 1)
                   or (e.get("type") == "guard" and e.get("kind") == "parcel_context"
                       and e.get("parcel_count", 0) > 1)
                   for e in trial.get("events", []))
    return sum(exposed(t) for t in trials) / max(1, len(trials))


def ambiguous_parcel_rate(trials):
    """Guard handoffs before any write, requiring parcel clarification."""
    return sum(any(e.get("type") == "guard" and e.get("kind") == "ambiguous_parcel"
                   for e in t.get("events", [])) for t in trials) / max(1, len(trials))


MONITORS = {
    "multi_parcel_exposure_rate": multi_parcel_exposure_rate,
    "ambiguous_parcel_rate": ambiguous_parcel_rate,
    "escalation_rate": escalation_rate,     # có sẵn; KHÔNG tính là metric mới của đội
}
STARTER_MONITORS = ("escalation_rate",)
