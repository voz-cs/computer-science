# 📜 L08: FUNCTIONS AS OBJECTS, SCOPE

**Cảnh giới:** Luyện Khí Tầng 08 | **Môn phái:** MIT 6.100L | **Trạng thái:** [ĐẠI THÀNH 🟢]

---

> _"Vạn vật đều là linh khí, và Hàm (Function) cũng vậy. Khi đạo hữu nhận ra một Hàm có thể được truyền đi như một thanh kiếm, hoặc được trả về như một viên đan dược, đạo hữu đã chạm tay vào cảnh giới của sự biến hóa khôn lường."_

## ⚔️ ĐẠO LÝ L08 (Functions as First-Class Citizens)

Trong tầng này, chúng ta sẽ học cách hóa giải sự cứng nhắc của code bằng cách coi Hàm như một đối tượng:

1. **Hàm là Đối tượng (Functions as Objects):** Hàm có thể được gán cho biến, truyền vào hàm khác (Higher-order functions), hoặc được trả về từ hàm khác.
2. **Môi trường & Phạm vi (Environments & Scope):** Hiểu sâu về cách Python quản lý linh lực tại từng tầng không gian khi hàm được thực thi.
3. **Hàm Lambda:** Những tiểu trận pháp ẩn danh, nhanh gọn và sắc bén.

---

## 🐉 ĐỘNG PHỦ LUYỆN TẬP (Finger Exercises)

Các bí kíp cần hóa giải trong chương này:

- [ ] **same_chars(s1, s2):** So sánh linh ấn giữa hai chuỗi. Đảm bảo mọi ký tự trong s1 đều có mặt trong s2 và ngược lại.

Toàn bộ code được phong ấn tại [finger_exercises.py](file:///c:/Users/manhthanh/Glogos/computer-science/courses/01-intro-cs-mit/L08-functions-as-objects/finger_exercises.py).

---

## 💬 LỜI NHẮN ĐỒNG ĐẠO (VOZ)

"Anh em ơi, học đến đây là bắt đầu 'hacking' thực sự rồi đấy. Coi hàm như một object chính là chìa khóa để viết code cực ngắn và cực thông minh. Đừng để Scope làm anh em lú lẫn, hãy cứ bám sát linh đồ (Environment diagrams) mà tu luyện!"

---

_Lưu trữ tại tàng kinh các L08-functions-as-objects_
