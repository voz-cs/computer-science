# 10: Dictionaries (Từ điển)

Dictionary là một tập hợp các cặp **Key - Value** (Khóa - Giá trị). Nó giống như List nhưng linh hoạt hơn vì Index (Key) có thể là gần như bất kỳ kiểu dữ liệu nào (thường là String).

## 1. Thao tác cơ bản
- **Khởi tạo**: `d = dict()` hoặc `d = {}`
- **Thêm/Sửa**: `d['key'] = 'value'`
- **Truy cập**: `print(d['key'])` (Lỗi `KeyError` nếu không tồn tại)
- **Đếm phần tử**: `len(d)`
- **Kiểm tra tồn tại**: `'key' in d` (Trả về True/False)
- **Lấy danh sách giá trị**: `list(d.values())`

## 2. Hàm `get()` - Kỹ thuật quan trọng nhất
Thay vì dùng `if/else` để kiểm tra key có tồn tại hay không trước khi cộng dồn, ta dùng `get(key, default)`:
```python
counts = dict()
for word in words:
    counts[word] = counts.get(word, 0) + 1
```
*Ghi chú: Nếu `word` chưa có trong `counts`, nó sẽ lấy giá trị mặc định là `0` rồi cộng thêm `1`.*

## 3. Duyệt Dictionary
- **Duyệt qua Key**:
```python
for key in counts:
    print(key, counts[key])
```
- **Duyệt theo thứ tự bảng chữ cái**:
```python
lst = list(counts.keys())
lst.sort()
for key in lst:
    print(key, counts[key])
```

## 4. Xử lý văn bản (Nâng cao)
Để đếm từ chính xác, cần loại bỏ dấu câu và chuyển về chữ thường:
```python
import string
line = line.translate(line.maketrans("", "", string.punctuation))
line = line.lower()
```

## 5. Danh sách bài tập (Exercises)
- **Ex 2**: Đếm số tin nhắn theo ngày trong tuần (từ dòng "From...").
- **Ex 3**: Lập biểu đồ tần suất (histogram) địa chỉ email người gửi.
- **Ex 4**: Tìm người gửi nhiều tin nhắn nhất (dùng vòng lặp tìm Max).
- **Ex 5**: Đếm số lượng tin nhắn theo tên miền (domain) của email.