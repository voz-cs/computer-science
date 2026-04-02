# Lecture 2: Strings, Input/Output, and Branching

Mục tiêu của chương này là cung cấp các công cụ để chương trình có tính tương tác (Interaction) và khả năng ra quyết định (Decision Making).

## 1. Strings (Chuỗi ký tự)
- **Định nghĩa:** Chuỗi các ký tự nằm trong nháy đơn `'...'` hoặc nháy kép `"..."`.
- **Thao tác cơ bản:**
  - Concatenation (Nối chuỗi): `'apple' + 'pie' == 'applepie'`
  - Repetition (Lặp chuỗi): `'ha' * 3 == 'hahaha'`
  - Length (Độ dài): `len('hello') == 5`

## 2. Input & Output
- **Output:** Sử dụng hàm `print()`. 
  - Khuyên dùng **f-strings**: `print(f"Giá trị là {x}")`.
- **Input:** Sử dụng hàm `input()`.
  - **Cực kỳ quan trọng:** `input()` LUÔN trả về một **String**. Nếu muốn tính toán số học, phải ép kiểu: `int(input("Nhập số: "))`.

## 3. Branching (Rẽ nhánh)
Cho phép máy tính đi theo các luồng khác nhau dựa trên điều kiện đúng/sai.

### Cấu trúc:
```python
if <điều kiện 1>:
    <khối lệnh A>
elif <điều kiện 2>:
    <khối lệnh B>
else:
    <khối lệnh C>
```

### Các toán tử so sánh (Comparison):
`==`, `!=`, `<`, `>`, `<=`, `>=`

### Các toán tử logic (Logic):
`and`, `or`, `not`

---
*"Debug early, debug often."*
