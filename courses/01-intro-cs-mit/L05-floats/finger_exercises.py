# 📜 Luyện Khí Tầng 05: Đạo của sự Sai Số (Floats and Approximation)
# Course: MIT 6.100L

import math
import sys
import io

# Đảm bảo terminal hỗ trợ UTF-8 để hiển thị linh ngữ (Vietnamese)
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def check_float_mystery():
    """
    Khác với số nguyên (integers) có linh khí thuần khiết, 
    số thực (floats) luôn mang theo một chút "tạp niệm".
    """
    x = 0.1 + 0.1 + 0.1
    print(f"Linh lực của 0.1 + 0.1 + 0.1 là: {x}")
    print(f"Liệu nó có bằng 0.3 không? -> {x == 0.3}")
    
    # Khẩu quyết: Luôn dùng Epsilon để so sánh
    epsilon = 0.00001
    if abs(x - 0.3) < epsilon:
        print("=> Chúc mừng đạo hữu! Đã dùng Epsilon để chế ngự sai số.")

def square_root_newton(y, epsilon=0.0001):
    """
    Tìm căn bậc hai của y dùng "Newton-Raphson Tâm Pháp".
    Chiêu thức này dùng đạo hàm để bẻ cong không gian, tiệm cận nghiệm nhanh gấp vạn lần Guess-and-Check.
    """
    if y < 0:
        # Căn bậc hai của số âm là phạm vào "ma đạo" (với integers/floats), ta không tu hành ở đây.
        return None, 0
    
    # Khởi đầu từ "trung đạo": chọn điểm đoán bằng một nửa y để làm mốc xuất phát.
    guess = y / 2.0
    iterations = 0
    
    # Vòng lặp "Tầm Đạo": tiếp tục chừng nào sai số vẫn còn lớn hơn Epsilon (vùng linh lực cho phép).
    while abs(guess**2 - y) >= epsilon:
        # TÂM PHÁP ĐẠO HÀM (Newton-Raphson Formula):
        # Ta không đoán mò, mà dùng đạo hàm (tiếp tuyến) để bẻ cong không gian, tiệm cận nghiệm siêu tốc.
        # Công thức: g_mới = g_cũ - f(g)/f'(g) => g - (g^2 - y) / (2 * g)
        guess = guess - (((guess**2) - y) / (2 * guess))
        iterations += 1
        
    return guess, iterations

def square_root_exhaustion(y, epsilon=0.0001, step=0.001):
    """
    Tìm căn bậc hai của y dùng "Successive Approximation" (Mò Kim Đáy Bể).
    Chiêu thức sơ đẳng nhất: đi bộ từng bước nhỏ cho đến khi chạm đến chân lý.
    """
    if y < 0:
        return None, 0
        
    guess = 0.0
    iterations = 0
    
    while abs(guess**2 - y) >= epsilon and guess**2 <= y:
        guess += step
        iterations += 1
        
    if abs(guess**2 - y) < epsilon:
        return guess, iterations
    else:
        return None, iterations

def square_root_bisection(y, epsilon=0.0001):
    """
    Tìm căn bậc hai của y dùng "Bisection Search" (Giải thuật Phân Quy Tắc).
    Chiêu thức "Chia để trị", tuy không nhanh bằng Newton nhưng cực kỳ vững chãi.
    """
    if y < 0:
        return None, 0
        
    low = 0.0
    high = max(1.0, y)
    guess = (low + high) / 2.0
    iterations = 0
    
    while abs(guess**2 - y) >= epsilon:
        # Khẩu quyết: Nếu bình phương lớn quá, hạ cánh trên. Nhỏ quá, nâng cánh dưới.
        if guess**2 < y:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        iterations += 1
        
    return guess, iterations

def compare_sqrt_methods(target_value):
    """
    Đại Hội So Tài giữa các giải thuật tìm căn.
    """
    print(f"\n--- ĐẠI HỘI SO TÀI: TÌM CĂN BẬC HAI CỦA {target_value} ---")
    
    # 1. Newton-Raphson
    res_n, iter_n = square_root_newton(target_value)
    print(f"🔹 Newton-Raphson:  Kết quả = {res_n:.6f} | Tiêu tốn {iter_n} lần vận công.")
    
    # 2. Bisection Search
    res_b, iter_b = square_root_bisection(target_value)
    print(f"🔹 Bisection Search: Kết quả = {res_b:.6f} | Tiêu tốn {iter_b} lần vận công.")
    
    # 3. Successive Approximation (Exhaustion)
    # Lưu ý: Với số lớn, step nhỏ, phương pháp này rất chậm.
    # Ta dùng step=0.001 và epsilon=0.1 để nó có cơ hội tìm thấy nghiệm trong thời gian hợp lý.
    res_e, iter_e = square_root_exhaustion(target_value, epsilon=0.1, step=0.001) 
    if res_e:
        print(f"🔹 Exhaustion Method: Kết quả = {res_e:.6f} | Tiêu tốn {iter_e} lần vận công.")
    else:
        print(f"🔹 Exhaustion Method: Thất bại (Linh lực cạn kiệt hoặc bước quá thô).")
        
    print("\n--- KẾT LUẬN ---")
    if res_e:
        print(f"🔥 Newton-Raphson nhanh gấp {iter_e/iter_n:.1f} lần Exhaustion!")
    print(f"🔥 Newton-Raphson nhanh gấp {iter_b/iter_n:.1f} lần Bisection!")

if __name__ == "__main__":
    check_float_mystery()
    
    target = 1234.56  # Chọn con số vừa phải để thấy sự chênh lệch rõ rệt
    compare_sqrt_methods(target)


