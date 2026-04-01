# Chapter 12: Regular Expressions - Siêu năng lực xử lý văn bản

Regular Expressions (Regex) là một ngôn ngữ cực kỳ mạnh mẽ để tìm kiếm và trích xuất dữ liệu từ văn bản. Thay vì dùng nhiều câu lệnh `if` và `split()`, Regex cho phép bạn dùng các "khuôn mẫu" (patterns).

## 1. Các ký tự "quyền năng" (Meta-characters)
- `^` : Khớp với phần bắt đầu của dòng.
- `$` : Khớp với phần kết thúc của dòng.
- `.` : Khớp với bất kỳ ký tự nào ngoại trừ dòng mới.
- `\s` : Khớp với một khoảng trắng.
- `\S` : Khớp với một ký tự KHÔNG phải khoảng trắng.
- `*` : Lặp lại 0 hoặc nhiều lần.
- `*?` : Lặp lại 0 hoặc nhiều lần (Non-greedy).
- `+` : Lặp lại 1 hoặc nhiều lần.
- `+?` : Lặp lại 1 hoặc nhiều lần (Non-greedy).
- `[aeiou]` : Khớp với một ký tự duy nhất trong tập hợp.
- `[^XYZ]` : Khớp với một ký tự duy nhất KHÔNG nằm trong tập hợp.
- `[a-z0-9]` : Khớp với một chữ cái thường hoặc chữ số.
- `(` và `)` : Vùng bắt đầu và kết thúc để trích xuất dữ liệu (Extraction).

## 2. Các hàm quan trọng (Python default library `re`)
```python
import re

# Kiểm tra xem có khớp không
if re.search('^From:', line):
    print(line)

# Tìm và trích xuất dữ liệu (Trả về list)
emails = re.findall('\S+@\S+', line)
```

## 3. Tham lam (Greedy) vs Không tham lam (Non-greedy)
- Mặc định các ký tự `*` và `+` là **Greedy** (tìm chuỗi dài nhất có thể).
- Thêm dấu `?` phía sau (`*?` hoặc `+?`) để chuyển sang **Non-greedy** (tìm chuỗi ngắn nhất).

## 4. Bài tập thực hành
- `exercise_01.py`: Giả lập lệnh `grep` của Linux.
- `exercise_02.py`: Trích xuất số Revision và tính trung bình cộng.
- `assignment.py`: Trích xuất số và tính tổng.
