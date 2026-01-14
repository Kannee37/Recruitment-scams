# Lừa đảo tuyển dụng
## Tổng quan
Tuyển dụng trực tuyến là một cầu nối phổ biến, thuận tiện và nhanh chóng cho nhà tuyển dụng và người tìm việc. Tuy nhiên, sự bùng nổ của các nền tảng trực tuyến cũng kéo theo sự gia tăng của các hình thức lừa đảo tuyển dụng, gây thiệt hại về tài chính, tinh thần và thậm chí là an toàn cá nhân cho nhiều người lao động, đặc biệt là giới trẻ, sinh viên và thậm chí cả người trung niên.

Dự án này tập trung vào việc xây dựng pipeline thu thâp và xử lý dữ liệu bài đăng tuyển dụng trên nền tẳng mạng xã hội phổ biến nhất hiện nay - Facebook - nơi có nhiều bài đăng tuyển dụng phi chính thống. 

Các bước thực hiện bao gồm:
* Thu thập vài đăng thông qua selenium
* Phân tích nội dung, gán nhãn thủ công
* Tiền xử lý văn bản
* Chuẩn hóa thông tin
* Loại bỏ trùng lặp
* Tạo đặc trưng cho mô hình học máy

## Kết quả
### Kết quả thu thập dữ liệu
[Dữ liệu ban đầu](https://docs.google.com/spreadsheets/d/1HcWa648YSfHfKRqu0JBO16XM54FoC6fDTknBEkhxvvU/edit?usp=sharing) (sau khi thu thập) gồm 6.857 dòng, tương ứng với các bài đăng hoặc bình luận tuyển dụng được trích xuất từ các hội nhóm tuyển dụng trên Facebook, bao gồm các trường: 
* link - đường dẫn đến bài đăng
* author - tác giả, người đăng bài
* content - nội dung bài đăng
* crawl_time - thời gian bài đăng được thu thập

### Kết quả phân tích nội dung và tiền xử lý
Dữ liệu sau thu thập được phân tích thành các nội dung:
* Tài khoản (xét xem tài khoản đăng bài có đáng tin cậy không)
* Vị trí làm (Vị trí bài đăng tuyển dụng)
* Nhóm ngành nghề
* Lương
* Thời gian làm
* Hình thức làm (online - offline - unknow)
* Hình thức nhận việc (hình thức mà ứng viên dùng để liên lạc với nhà tuyển dụng)
* Mô tả công việc (xem xét mức độ mô tả chi tiết về vị trí tuyển dụng)
* Nhãn (Lừa đảo - Thật - Unknow)
* Lí do (Ghi chú lại cơ sở hoặc dấu hiệu để gán nhãn bài đăng)

Sau quá trình phân tích và xử lý dữ liệu, dữ liệu còn lại 580 dòng thuộc hai nhãn chính: Thật và Lừa đảo.

## Công cụ
* Python 
* Pandas, Numpy
* Selenium

## Ghi chú
Xem chi tiết tại file: BaoCaoThucTap.pdf
