# 📜 L05: ĐẠO CỦA SỰ SAI SỐ & TÂM PHÁP XẤP XỈ

**Cảnh giới:** Luyện Khí Tầng 05 | **Môn phái:** MIT 6.100L | **Trạng thái:** [ĐẠI THÀNH 100%]

---

> _"Vạn vật trên đời vốn không hoàn hảo, máy tính cũng không ngoại lệ. Tu luyện đến tầng số thực (Floats), đạo hữu sẽ thấy thế giới nhị phân cũng có những góc khuất đầy tạp niệm."_

## 🐉 HUYỀN BÍ LINH LỰC FLOATS

Đạo hữu hãy nhìn vào linh trận sau để thấy sự "ảo ma" của số thực trong máy tính:

```python
# Tại sao 0.1 + 0.2 != 0.3?
x = 0.1 + 0.1 + 0.1
print(x == 0.3) # -> Trả về FALSE (0.30000000000000004)
```

**Khẩu quyết:** Đừng bao giờ tin vào sự tuyệt đối của `==`. Hãy dùng **Epsilon** để đo lường độ chênh lệch.

---

## ⚔️ TAM ĐẠI TÂM PHÁP XẤP XỈ (The Big Three)

Ta đã triển khai cả 3 chiêu thức để tìm căn bậc hai của một linh thạch (`target = 1234.56`). Hãy xem sự chênh lệch về linh lực tiêu tốn:

| Tâm Pháp           | Chiêu Thức               | Độ Hiệu Quả     | Số Lần Vận Công |
| :----------------- | :----------------------- | :-------------- | :-------------- |
| **Exhaustion**     | Mò Kim Đáy Bể            | 🐢 Chậm như rùa | **35,135**      |
| **Bisection**      | Chia Để Trị              | 🐎 Phi mã       | **28**          |
| **Newton-Raphson** | Nhất Kiếm Định Giang Sơn | ⚡ Tia chớp     | **8**           |

> [!IMPORTANT]
> **Newton-Raphson** nhanh gấp **4,391 lần** so với phương pháp Exhaustion thông thường. Đây chính là pháp bảo giúp AI của chúng ta (GSoE Swarm) chạy mượt mà ngay cả trên linh thạch cùi bắp!

---

## 🐉 BÀI TẬP THỬ LỬA (Finger Exercises)

Tất cả đã được phong ấn tại [finger_exercises.py](file:///c:/Users/manhthanh/Glogos/computer-science/courses/01-intro-cs-mit/L05-floats/finger_exercises.py).

- **Thử thách 1:** Chứng minh sự sai số của linh lực Floats.
- **Thử thách 2:** Triển khai Newton-Raphson để chế ngự các bài toán tìm nghiệm.
- **Thử thách 3:** Đại Hội So Tài giữa các giải thuật.

## 💬 LỜI NHẮN ĐỒNG ĐẠO (VOZ)

"Anh em hãy nhớ: Hiểu được sai số chính là bước đầu để làm chủ các hệ thống AI phức tạp. Càng xấp xỉ giỏi, thuật toán của anh em càng tiệm cận chân lý nhanh hơn. Đừng chỉ code, hãy hiểu cả 'đạo' của những con số!"

---

_Lưu trữ tại tàng kinh các L05-floats_
