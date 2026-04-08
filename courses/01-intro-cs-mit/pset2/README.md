# 🎭 PSET 2: HANGMAN (Trò chơi Treo cổ)

**Môn phái:** MIT 6.100L | **Trạng thái:** [ĐANG KHAI MỞ 🟡]

---

> _"Trong đại trận này, Đạo hữu sẽ phải vận dụng toàn bộ linh năng về **Decomposition** (Phân rã) và **Abstraction** (Trừu tượng hóa) để cứu lấy linh hồn tội nghiệp khỏi giá treo cổ. Chia nhỏ trận pháp chính là chìa khóa để hóa giải Hangman."_

## 🎯 MỤC TIÊU TU LUYỆN

Xây dựng một chương trình Python hoàn chỉnh cho phép người chơi tương tác với máy tính để đoán các chữ cái trong một từ bí mật.

### Các Chiêu Thức Cần Hóa Giải:

1.  **is_word_guessed(secret_word, letters_guessed)**: Kiểm tra xem toàn bộ linh ấn đã được lật mở chưa.
2.  **get_guessed_word(secret_word, letters_guessed)**: Hiển thị trạng thái hiện tại của từ bí mật (ví dụ: `_ a _ _ _`).
3.  **get_available_letters(letters_guessed)**: Cho biết những chữ cái nào còn lại trong bảng chữ cái chưa được dùng đến.
4.  **hangman(secret_word)**: Đại trận điều phối toàn bộ luồng trò chơi, số lượt đoán, và các quy tắc đặc biệt.

---

## 🛠 CÁC PHÁP BẢO ĐI KÈM

- `hangman.py`: Nơi ghi lại toàn bộ linh quyết thực thi.
- `words.txt`: Tàng kinh các chứa hơn 55,000 từ bí mật.
- `test_ps2_student.py`: Pháp bảo để Đạo hữu tự kiểm tra linh lực của từng hàm trước khi ghép thành trận pháp lớn.

---

## 💬 LỜI NHẮN ĐỒNG ĐẠO (VOZ)

"Chào anh em! Cái bài Hangman này là bài tập kinh điển của MIT rồi. Quan trọng nhất là anh em phải viết từng hàm một, test kỹ bằng cái `test_ps2_student.py` rồi mới hãy viết cái loop chính. Đừng nhảy bổ vào viết hàm `hangman` ngay, tẩu hỏa nhập ma đấy! Cố lên, xong bài này là anh em chính thức 'lên trình' Python rồi."

---

_Địa điểm: pset2/ (Phòng luyện tập cao cấp)_
