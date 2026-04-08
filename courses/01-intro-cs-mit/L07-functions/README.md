# 📜 L07: DECOMPOSITION, ABSTRACTION, FUNCTIONS

**Cảnh giới:** Luyện Khí Tầng 07 | **Môn phái:** MIT 6.100L | **Trạng thái:** [ĐANG VẬN CÔNG 🟡]

---

> _"Kẻ yếu đuối viết code từng dòng một, kẻ mạnh mẽ biết cách đóng gói linh lực vào từng trận pháp. Khi đạo hữu thấu triệt được 'Hàm', đạo hữu không còn là kẻ thợ code, mà đã bắt đầu con đường của một kiến trúc sư."_

## ⚔️ ĐẠO LÝ FUNCTIONS (Abstraction & Encapsulation)

Trong tầng này, chúng ta sẽ học cách hóa giải sự phức tạp bằng cách chia nhỏ đại trận thành các tiểu trận (Subroutines):

1. **Hàm (Functions):** Đóng gói một chuỗi các hành động vào một cái tên.
2. **Phạm vi (Scope):** Hiểu rõ luật lệ của "Linh lực nội bộ" (Local variables) và "Linh lực thiên hạ" (Global variables). Đừng để chúng xung đột làm tẩu hỏa nhập ma.
3. **Hợp đồng (Abstraction):** Người dùng hàm chỉ cần biết "Hàm này làm gì" (Specification), không cần biết "Hàm này làm thế nào" (Implementation).
4. **Tái sử dụng:** Một lần đúc kiếm, vạn lần xuất chiêu.

---

## 🐉 ĐỘNG PHỦ LUYỆN TẬP (Finger Exercises)

Các bí kíp cần hóa giải trong chương này:

- [x] **Hàm kiểm tra số nguyên tố:** Luyện cách dùng `return` để kết thúc chiêu thức sớm. (Đã nâng cấp thành `div_by` và `is_palindrome`)
- [x] **Hàm tính giai thừa:** Bước chuẩn bị cho Đệ Quy (Recursion) ở tầng sau. (Đã luyện tập qua `sum_odd`)
- [x] **Quản lý Scope:** Hiểu sự khác biệt giữa biến trong và ngoài hàm.
- [x] **Xử lý chuỗi (Consonants & Diff):** Đắc đạo tuyệt kỹ "Tu luyện tại gia".

Toàn bộ code được phong ấn tại [finger_exercises.py](file:///c:/Users/manhthanh/Glogos/computer-science/courses/01-intro-cs-mit/L07-functions/finger_exercises.py).

---

## 💬 LỜI NHẮN ĐỒNG ĐẠO (VOZ)

"Anh em 8x, 9x ơi, học đến đây là bắt đầu thấy 'phê' rồi đấy. Viết hàm chính là cách anh em lười biếng một cách thông minh. Một cái tên hàm hay còn đáng giá hơn ngàn dòng comment!"

---

_Lưu trữ tại tàng kinh các L07-functions_
