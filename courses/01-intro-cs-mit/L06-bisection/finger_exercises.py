# 📜 Luyện Khí Tầng 06: Tâm Pháp Đa Thức (Polynomials & Newton-Raphson)
# Course: MIT 6.100L
# Mục tiêu: Tìm nghiệm đa thức tổng quát dùng Newton-Raphson & Bisection.

import sys
import io

# Đảm bảo terminal hỗ trợ UTF-8 để hiển thị linh ngữ (Vietnamese)
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def cube_root_bisection(cube, epsilon=0.01):
    """
    Tìm căn bậc ba của cube dùng Bisection Search.
    """
    low = min(cube, 0, 1) 
    high = max(cube, 0, 1)
    guess = (low + high) / 2.0
    num_guesses = 0
    while abs(guess**3 - cube) >= epsilon:
        if guess**3 < cube:
            low = guess
        else:
            high = guess
        guess = (low + high) / 2.0
        num_guesses += 1
    return guess, num_guesses

def evaluate_poly(coeffs, x):
    """
    Tính giá trị đa thức: p(x) = a_n*x^n + ... + a_1*x + a_0
    coeffs: List các hệ số [a_n, ..., a_0]
    """
    total = 0
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs):
        total += coeff * (x**(degree - i))
    return total

def derive_poly(coeffs):
    """
    Tính đạo hàm của đa thức: p'(x)
    """
    new_coeffs = []
    degree = len(coeffs) - 1
    for i, coeff in enumerate(coeffs[:-1]):
        new_coeffs.append(coeff * (degree - i))
    return new_coeffs

def newton_raphson_poly(coeffs, guess, epsilon=0.0001, max_iters=100):
    """
    Tâm pháp Newton-Raphson tổng quát cho mọi đại trận đa thức.
    """
    num_guesses = 0
    while abs(evaluate_poly(coeffs, guess)) >= epsilon and num_guesses < max_iters:
        val = evaluate_poly(coeffs, guess)
        diff = evaluate_poly(derive_poly(coeffs), guess)
        
        if diff == 0: # Tránh trường hợp đạo hàm bằng 0 (lạc lối)
            break
            
        # Khẩu quyết: Tiệm cận nghiệm bằng tiếp tuyến
        guess = guess - (val / diff)
        num_guesses += 1
        
    if num_guesses >= max_iters:
        return None, num_guesses
    return guess, num_guesses

def safe_newton_poly(coeffs, low, high, epsilon=0.0001):
    """
    Hộ Thân Pháp Trận: Kết hợp Newton-Raphson và Bisection.
    Luôn đảm bảo nghiệm nằm trong khoảng [low, high].
    """
    num_guesses = 0
    guess = (low + high) / 2.0
    
    # Kiểm tra điều kiện đổi dấu (bracket)
    f_low = evaluate_poly(coeffs, low)
    f_high = evaluate_poly(coeffs, high)
    if f_low * f_high > 0:
        return None, 0 # Không có rào chắn hợp lệ
        
    while abs(evaluate_poly(coeffs, guess)) >= epsilon:
        val = evaluate_poly(coeffs, guess)
        diff = evaluate_poly(derive_poly(coeffs), guess)
        
        # Thử vận công Newton
        guess_new = None
        if diff != 0:
            guess_new = guess - (val / diff)
            
        # Kiểm tra nếu Newton "nhảy bậy" ra ngoài rào chắn hoặc không thể tính toán
        if guess_new is None or guess_new < low or guess_new > high:
            # Cứu giá bằng Bisection
            guess_new = (low + high) / 2.0
        
        # Cập nhật rào chắn (Update bracket)
        if evaluate_poly(coeffs, low) * evaluate_poly(coeffs, guess_new) <= 0:
            high = guess_new
        else:
            low = guess_new
            
        guess = guess_new
        num_guesses += 1
        
        if num_guesses > 100: # Tránh lặp vô hạn nếu có lỗi
            break
            
    return guess, num_guesses

def run_poly_demo():
    """
    Trình diễn sức mạnh của Tâm Pháp Đa Thức trên các mẫu phổ biến.
    """
    # [Hệ số], Tên trận pháp, Điểm đoán đầu (initial guess)
    demo_cases = [
        ([1, 0, -24], "Căn bậc hai của 24 (x^2 - 24)", 2.0),
        ([1, 0, 0, -27], "Căn bậc ba của 27 (x^3 - 27)", 5.0),
        ([1, 0, -2, 2], "Trận pháp Luân Hồi (x^3 - 2x + 2)", 0.0), # Newton dễ bị lặp giữa 0 và 1
        ([1, -1, 4, -4], "Đại trận bậc ba (x^3 - x^2 + 4x - 4)", 5.0)
    ]
    
    print("--- ĐẠI HỘI CHIÊU THỨC: TÌM NGHIỆM ĐA THỨC ---")
    print(f"{'Trận pháp':<35} | {'Newton':<15} | {'Safe Newton':<15}")
    print("-" * 75)
    
    for coeffs, name, init_guess in demo_cases:
        # Tìm rào chắn (bracket) tự động cho Safe Newton
        low, high = init_guess, init_guess
        # Mở rộng vùng tìm kiếm cho đến khi thấy đổi dấu hoặc quá giới hạn
        for i in range(1, 20):
            low = init_guess - i * 2
            high = init_guess + i * 2
            if evaluate_poly(coeffs, low) * evaluate_poly(coeffs, high) <= 0:
                break
        
        res_n, iters_n = newton_raphson_poly(coeffs, init_guess)
        res_s, iters_s = safe_newton_poly(coeffs, low, high)
        
        n_display = f"{res_n:7.4f} ({iters_n:2d})" if res_n else f"Lạc lối ({iters_n:2d})"
        s_display = f"{res_s:7.4f} ({iters_s:2d})" if res_s else "Lạc lối"
        
        print(f"{name:<35} | {n_display:<15} | {s_display:<15}")
    
    print("-" * 75)
    print("Khẩu quyết: Đạo hàm dẫn lối, Bisection hộ thân!")

if __name__ == "__main__":
    run_poly_demo()
