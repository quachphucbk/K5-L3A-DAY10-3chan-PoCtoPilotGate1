# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): 3chan
- Lớp: L3A
- Repo của bàn: https://github.com/quachphucbk/K5-L3A-DAY10-3chan-PoCtoPilotGate1
- Thẻ sự cố đã bốc (S1–S8): S6

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Quách Ngọc Phúc |      2A202603665| Kỹ sư cổng |             x|
|   2 | Nguyễn Đức Minh          | 2A202603633     |Vận hành và pháp lý|             |
|   3 |           Ngô Văn Tuân|      2A202603630|     Sản phẩm và kinh doanh|             |
|   4 |    Hồ Quốc Toản       | 2A202603668   |   Kỹ sư cổng  |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## NgoVanTuan-2A202603630

### Phần việc phụ trách

Sản phẩm và kinh doanh: B3, phần kinh doanh B6, B7.4; C3.2, C5, phần kinh doanh C7, risk register C10 và đề xuất v2 C12. Đối chiếu trace và các phần phân tích kỹ thuật của Quách Ngọc Phúc để nối tác hại với quyết định kinh doanh; không ghi nhận phần kỹ thuật của đồng đội là của mình.

### Đóng góp cụ thể

- Đặt cổng business và giải thích chi phí/ROI, giữ nguyên tiêu chí đã ký; đo từng thay đổi ở B0.
- Sau khi nhận S6, phân biệt tiền hoàn theo đơn với trách nhiệm theo kiện; chỉ ra ca thiếu parcel_id vẫn ghi tiền và ca guard deny làm thiếu fault/notify đúng.
- Đối chiếu bản sửa S6 của Kỹ sư cổng trên main 497d9a5; after đạt 40/40 trong scope, không hoàn sai/lỗi oan/PII, ROI 0,36. Đề xuất giữ Thu hẹp HN/HCM, xem lại 25/11/2026, cần nhóm xác nhận; chưa phải phê duyệt pilot thật.
- Dùng Codex hỗ trợ đọc dữ liệu/trace, tính và kiểm tra số liệu, soạn phiếu/JSON và thực hiện Git. Các ngưỡng, phân công và quyết định cuối cần bản thân cùng nhóm kiểm tra, giải thích và xác nhận.

### Bằng chứng

Commit business `1684f51`, hợp nhất Phiếu B `76a308e`/`35735e4`; nhập thẻ S6 `581b1dd`, hồ sơ nhận thẻ `7bb1c43`. Report trước sửa R-S6-grade-20261118-165047-b7ef74; đối chiếu sau sửa R-S6-grade-20261118-170718-bc2890 và R-base-after-20261118-170747-bc2890; trace S6-01@11 (base/prepared), S6-21@11 (prepared); kiểm bổ sung S6-product-full-scope-verification.json và S6-product-cost-sensitivity.json trong runs/. Nội dung Phiếu C C3.2/C5 giả định/C7 kinh doanh/C10/C11 chi phí/C12; code guard/monitor S6 do Kỹ sư cổng làm, chưa có kết quả test ẩn.

### Exit ticket

Chờ Ngô Văn Tuân tự viết điều học được và điều còn chưa chắc sau khi kiểm tra phần việc; không ghi thay phản hồi cá nhân.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
