# 🛠️ MIT 6.100L: Software Setup Guide

Tài liệu này tóm tắt hướng dẫn cài đặt từ **Problem Set 0** của MIT.

## 1. Cài đặt Python (The Core)

MIT khuyến nghị sử dụng **Python 3.10** hoặc mới hơn.

- **Cách thức:** Sử dụng bản cài từ `python.org` hoặc thông qua **Anaconda/Miniconda**.
- **Kiểm tra:** `python --version` (Kết quả phải >= 3.10).

## 2. Lựa chọn IDE (The Interface)

- **Lựa chọn của MIT:** **Spyder** (đi kèm Anaconda) — Rất tốt cho người mới, giao diện giống MATLAB.
- **Lựa chọn cho Dev chuyên nghiệp (Khuyên dùng):** **VS Code**.
  - Cài thêm Extension: `Python` (Microsoft).

## 3. Cài đặt Thư viện Thống kê & Khoa học

Trong PSET 0, MIT yêu cầu cài đặt và verify thư viện `numpy`.

- **Lệnh cài:** `pip install numpy matplotlib`

## 4. Quy trình làm bài (Workflow)

1.  Viết code trong file `.py`.
2.  Chạy code bằng Interpreter (F5 trong VS Code hoặc `python filename.py` trong terminal).
3.  Kiểm tra kết quả output.

## 5. Verify (PSET 0)

Để đảm bảo mọi thứ đã sẵn sàng, hãy thực hiện bài tập tại `courses/01-intro-cs-mit/pset0/ps0.py`. Nếu script này chạy không lỗi và in ra kết quả $log_2$, nghĩa là quá trình thiết lập đã thành công.
