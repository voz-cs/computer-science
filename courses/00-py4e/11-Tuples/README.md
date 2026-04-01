# Chapter 11: Tuples - Mindset-First Summary

> "Tuples are immutable, but their value in structured data is eternal."

## 1. Core Mindset: The Locked List
Nếu **List** là một "bảng nháp" để ghi chép và thay đổi linh hoạt, thì **Tuple** là một "hợp đồng" (immutable contract). Một khi đã khởi tạo, nội dung bên trong không thể bị thay đổi (`TypeError: 'tuple' object does not support item assignment`).

### Tại sao chúng ta dùng Tuple thay vì List?
- **Data Integrity**: Bảo mật dữ liệu. Đảm bảo các cấu trúc như `(latitude, longitude)` hoặc `(node_ip, port)` không bị phá vỡ trong quá trình chạy.
- **Performance**: Nhẹ hơn và nhanh hơn List.
- **Hashability**: Tuple có thể làm **Key** cho Dictionary (List thì không).

## 2. DSU Pattern: Decorate, Sort, Undecorate
Đây là kỹ thuật mạnh mẽ nhất khi kết hợp Tuple và List để sắp xếp dữ liệu phức tạp (như sắp xếp từ theo độ dài):

1. **Decorate**: Tạo một list các tuple `(length, word)`.
2. **Sort**: Sử dụng `sort()` của Python (mặc định sort theo phần tử đầu tiên của tuple).
3. **Undecorate**: Trích xuất lại phần tử gốc từ list đã sort.

## 3. Tuple Unpacking
Kỹ thuật gán biến siêu tốc:
```python
(name, age) = ("Glogos", 2)
# Hoặc không cần ngoặc
name, age = "Glogos", 2
```

## 4. Ứng dụng trong GSoE Swarm
Trong hệ thống Swarm, chúng ta sẽ sử dụng Tuple để định danh **Node ID** và **Region Mapping**. Tính bất biến giúp đảm bảo Identity của một Node không bị "lệch" khi truyền qua các layer của mạng lưới.

---

## Exercises Checklist
- [ ] `exercise_01.py`: Phân tích email, tìm người gửi nhiều nhất (Dùng (count, email) tuple).
- [ ] `exercise_02.py`: Phân phối giờ gửi email (Dùng (hour, count) tuple để sort).
- [ ] `exercise_03.py`: Tần suất chữ cái (a-z) giảm dần.
