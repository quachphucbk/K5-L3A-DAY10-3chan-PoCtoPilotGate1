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



## QuachNgocPhuc-2A202603665

### Phần việc phụ trách

Kỹ sư cổng và trưởng nhóm; phối hợp Hồ Quốc Toản ở phần kỹ thuật. Phụ trách thước đo bước ở Phiếu A A2; baseline, gate và trace tại B0–B2; phần kỹ thuật B5/B6; cổng và behavioral test B7.1–B7.3; chạy checkpoint/prepared để cung cấp bằng chứng B8. Sau khi nhận S6, phụ trách phân tích kỹ thuật C2/C4/C5-spec/C6, sửa cổng C7, monitor C8, fault tree sau sửa C9 và rủi ro kỹ thuật C10. File chính: `lab10/guards.py`, `lab10/monitors.py`, các phần kỹ thuật trong Phiếu B/C. Quyết định v1/v2 và ngưỡng là của cả nhóm; business do Ngô Văn Tuân, vận hành/pháp lý do Nguyễn Đức Minh phụ trách.

### Đóng góp cụ thể

- Tổng hợp tiêu chí Phiếu A cùng nhóm, đồng bộ ngưỡng được nhóm chốt sang JSON và đại diện ký, commit/push trước lần đánh giá đầu tiên; giữ nguyên tiêu chí sau ký.
- Đo baseline 110 trial và dò `T-002@55`: xác định agent dùng 5 ngày khách khai thay 2 ngày tracking, dẫn đến hoàn sai 20.000đ và ghi lỗi oan VNX; phân biệt chỉ số tổng đạt với điều kiện an toàn không đạt.
- Viết cổng vòng 1 kiểm quyền lợi/phê duyệt trước hoàn tiền, căn cứ kiện/hãng trước ghi lỗi và payload tối thiểu trước gửi hãng; ghim policy theo ngày hiệu lực. Chạy hai ticket mới tự khai trễ 9/12 ngày để kiểm cổng, sửa regression phát hiện trong quá trình thử và chốt snapshot vòng 1.
- Với S6, xác định ba nhánh: dùng kiện đầu thay kiện khách yêu cầu; thiếu parcel_id khi nhiều kiện trễ nhưng vẫn ghi tiền; thiếu trần lỗi hãng cộng dồn trong ngày. Sửa cổng ghi lỗi để dùng bộ tham số đúng kiện, chuyển người trước khi ghi khi yêu cầu mơ hồ, chặn lỗi hãng tự động vượt trần Ops mà vẫn giữ khoản hoàn hợp lệ.
- Thêm `multi_parcel_exposure_rate` và `ambiguous_parcel_rate` trong MONITORS, chỉ dùng sự kiện không có nhãn; giải thích đây là tín hiệu tiếp xúc/rủi ro và nhu cầu duyệt, không phải nhãn xác nhận lỗi oan.
- Kiểm tra regression bằng 13 test công khai, đánh giá phạm vi pilot và replay toàn bộ bộ nền/S6 trong bộ nhớ; ghi rõ khác biệt giữa số trial chính thức theo phạm vi với kiểm bổ sung toàn phạm vi. Giữ nguyên snapshot và tiêu chí đã ký; không xử lý riêng theo ID ticket/seed.
- Dùng Codex hỗ trợ đọc đề/code/trace, soạn Phiếu A và phần kỹ thuật Phiếu B/C, đề xuất/viết cổng và monitor, chạy kiểm tra và hỗ trợ Git. Bản thân chịu trách nhiệm đọc lại, giải thích cách hoạt động, giới hạn và bằng chứng; không coi nội dung AI soạn là xác nhận thay các thành viên.

### Bằng chứng

- Commit ký tiêu chí: `d77c361` (Sign acceptance criteria); hash tiêu chí `2def0fbb`. Commit phần kỹ sư Phiếu B: `9c9de60`; bản hoàn thiện vòng 1 `5da3d68`; phần sửa S6/phiếu kỹ thuật được lưu trong `497d9a5`.
- Baseline: `R-base-before-20261118-151704-b45eeb`, pass_rate 0.9909, pass_k 0.9545; trace `T-002@55` là bằng chứng nguyên nhân đầu vào ghi đè tracking.
- Vòng 1: after `R-base-after-20261118-163602-038c7e`; prepared `R-base-prepared-20261118-163627-038c7e`, 65/65 trial trong phạm vi đạt; snapshot hash `18b4521b`. Hai adhoc và kết quả ghi tại B7.3; đối chiếu full scope ở `runs/round1-full-scope-regression.json` đạt 110/110.
- S6: trace prepared/after `S6-01@11` (kiện đúng nhưng ghi sai đối tượng), `S6-20@11` (nhiều kiện trễ chưa rõ ý định). Sau sửa `S6-01` ghi đúng P2/VNX; `S6-20` chuyển người trước khi ghi, ledger/fault/outbound rỗng.
- Report sau sửa: `R-S6-after-20261118-170014-83599a`, S6 40/40 trong phạm vi đạt, hoàn sai/lỗi hãng oan/PII đều 0, chi phí 7.372đ/ticket, ROI 0.36; bộ nền `R-base-after-20261118-170014-83599a` đạt 65/65. Grade đối chiếu `R-S6-grade-20261118-170014-83599a` và lần chạy lại `R-S6-grade-20261118-170933-83599a` xác nhận after pass_rate=1.0; không nhầm với base=0.3333 hoặc prepared=0.375.
- Kiểm bổ sung `runs/S6-engineering-full-scope.json`: S6 60/60 và bộ nền 110/110 đạt; các ca S6-42/43 vẫn hoàn đúng nhưng không ghi thêm lỗi vượt trần. 13/13 test công khai đạt; chưa có kết quả test ẩn.

### Exit ticket

- **Điều học được:** agent có thể báo thành công và đạt pass_rate tổng cao nhưng vẫn gây tác hại ở sổ tiền hoặc sổ lỗi hãng. Cổng phải kiểm nguồn có thẩm quyền và đặt đúng thời điểm: với đơn nhiều kiện chưa rõ ý định, chặn tại bước ghi lỗi là quá muộn nếu tiền đã ra. Ba mốc base/prepared/after giúp phân biệt mức chuẩn bị và hiệu quả sửa sự cố.
- **Điều còn chưa chắc:** cổng đếm lỗi hãng hiện chạy trên sổ ngày tuần tự của mock; cần kiểm tính nguyên tử khi nhiều worker cùng ghi, ranh giới ngày, chất lượng tracking thật và năng lực người duyệt khi tải dồn. Kết quả lab chưa chứng minh các điều kiện này trong pilot thật.

## NguyenDucMinh-2A202603633

### Phần việc phụ trách

Sản phẩm và kinh doanh: B3, phần kinh doanh B6, B7.4; C3.2, C5, phần kinh doanh C7, risk register C10 và đề xuất v2 C12. Đối chiếu trace và các phần phân tích kỹ thuật của Quách Ngọc Phúc để nối tác hại với quyết định kinh doanh; không ghi nhận phần kỹ thuật của đồng đội là của mình.

### Đóng góp cụ thể

- Vận hành và pháp lý; phụ trách đánh giá tác động lên hãng vận chuyển, tài xế, khách hàng và người duyệt khi đưa trợ lý từ PoC sang pilot.
- Tham gia hoàn thiện phần HAZOP đối với file_carrier_fault, checklist dữ liệu/bảo mật/phân quyền/hiệu năng, năng lực người duyệt, quy trình đối soát và giới hạn trách nhiệm pháp lý.
- Phân tích nguy cơ ghi lỗi oan cho hãng/tài xế khi một đơn có nhiều kiện; đóng góp góc nhìn vận hành và pháp lý cho C3.2 (hình dung của các bên), C11 (runbook) và C12 (điều kiện quyết định Gate 1 v2).

### Exit ticket
- Điều học được: Một gate tốt không chỉ kiểm tra tính đúng của câu trả lời mà còn phải kiểm soát tác động thực tế của lệnh ghi tiền và quy trách nhiệm cho bên thứ ba; với đơn nhiều kiện, bằng chứng phải gắn đúng kiện/hãng/tài xế.
- Điều còn chưa chắc: Độ đầy đủ và độ trễ của dữ liệu tracking ngoài thực tế, năng lực xử lý của người duyệt khi lượng ca tăng, và liệu các monitor có phát cảnh báo kịp thời trong pilot thật hay không.

## HoVaTen-MSSV

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.
