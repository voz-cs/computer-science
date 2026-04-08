# 📜 L06: TÂM PHÁP PHÂN QUY TẮC (BISECTION SEARCH)

**Cảnh giới:** Luyện Khí Tầng 06 | **Môn phái:** MIT 6.100L | **Trạng thái:** [ĐẠI THÀNH 100%]

---

> _"Trong thế giới hỗn độn của hàng vạn con số, kẻ nào biết 'chia để trị' sẽ là kẻ làm chủ cuộc chơi. Một nhát kiếm chia đôi trời đất, thu hẹp vạn lý chỉ trong một chớp mắt."_

## ⚔️ ĐẠO LÝ BISECTION SEARCH (Chia Để Trị)

Nếu như **Guess-and-Check** (L04) là kiểu mò mẫm vụng về, và **Approximation** (L05) là kiểu đi bộ từng bước nhọc nhằn, thì **Bisection Search** chính là phép dịch chuyển không gian:

1.  **Xác định ranh giới:** Luôn giữ hai cực `low` và `high`.
2.  **Một nhát chia đôi:** Lấy trung điểm `guess = (low + high) / 2`.
3.  **Thu hẹp phạm vi:** Nếu `guess` quá lớn, ta bỏ nửa trên. Nếu quá nhỏ, ta bỏ nửa dưới.
4.  **Lặp lại:** Mỗi lần chém, không gian tìm kiếm giảm đi một nửa.

**Hiệu quả:** Để tìm một con số trong 1 triệu mẫu, Đạo hữu chỉ cần tối đa **20 lần** vận công chém đôi. (Linh lực Logarit bậc 2 của 1,000,000).

---

## 🐉 BÀI TẬP THỬ LỬA (Finger Exercises)

Tại động phủ này, ta đã tu luyện thành công:
- [x] **Tìm Căn Bậc Ba (Cube Root):** Giải thuật bisection search áp dụng cho cả số dương và số âm.
- [x] **Tâm Pháp Đa Thức (Newton-Raphson):** Nâng cấp lên khả năng hóa giải mọi đại trận $p(x) = 0$.
- [x] **Hộ Thân Pháp Trận (Safe Newton):** Tuyệt kỹ kết hợp sự thần tốc của Newton và sự chắc chắn của Bisection.

### 🏆 ĐẠI HỘI CHIÊU THỨC (Experimental Results)

Ta đã tổ chức một cuộc so tài giữa các tâm pháp trên các "Đại trận" đa thức. Kết quả cho thấy sự ưu việt của việc kết hợp chiêu thức:

| Trận pháp (Function) | Newton-Raphson | Safe Newton | Kết quả |
| :--- | :--- | :--- | :--- |
| **Căn bậc hai ($x^2-24$)** | 4 lần | 5 lần | Cân tài cân sức |
| **Luân Hồi ($x^3-2x+2$)** | **Lạc lối (100+)** | **7 lần** | **Safe Newton hóa giải hoàn toàn!** |

**Khẩu quyết bổ sung:** *"Nhanh là tốt, nhưng sống sót để về đích mới là đạo lý tối thượng."*

Toàn bộ code được phong ấn tại [finger_exercises.py](file:///c:/Users/manhthanh/Glogos/computer-science/courses/01-intro-cs-mit/L06-bisection/finger_exercises.py).

---

## 💬 LỜI NHẮN ĐỒNG ĐẠO (VOZ)

"Anh em 8x, 9x cày lại CS từ đầu chú ý nhé: Bisection Search không chỉ dùng để tìm căn, nó là nền móng cho rất nhiều thuật toán tối ưu sau này (như Binary Search trên mảng đã sắp xếp). Hiểu được nó, anh em sẽ không bao giờ phải 'mò kim đáy bể' một cách mù quáng nữa!"

---

_Lưu trữ tại tàng kinh các L06-bisection_
