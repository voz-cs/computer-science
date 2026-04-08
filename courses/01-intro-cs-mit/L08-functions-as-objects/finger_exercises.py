# 📜 Luyện Khí Tầng 08: Hàm là Đối tượng (Functions as Objects)
# Course: MIT 6.100L
# Mục tiêu: Thấu triệt Higher-order functions, Scope và Environments.

import sys
import io

# Đảm bảo terminal hỗ trợ UTF-8 để hiển thị linh ngữ (Vietnamese)
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def same_chars(s1, s2):
    """
    s1 và s2 là các chuỗi (strings).
    Trả về True nếu mọi ký tự trong s1 đều có mặt trong s2 và ngược lại.
    Nếu có bất kỳ ký tự nào chỉ xuất hiện trong một chuỗi, trả về False.
    """
    # Chiêu thức: Dùng Set (Linh tập) để thu gọn linh ấn
    # Ký tự duy nhất trong s1 và s2 phải giống hệt nhau.
    return set(s1) == set(s2)

def is_palindrome(s):
    """
    s là một chuỗi (string).
    Trả về True nếu s là chuỗi đối xứng, ngược lại False.
    """
    return s == s[::-1]

def f_yields_palindrome(n, f):
    """
    n là số nguyên dương.
    f là một hàm nhận vào int và trả về int.
    Trả về True nếu f(n) là một số đối xứng (palindrome).
    """
    # Chiêu thức: Chuyển kết quả f(n) thành chuỗi để kiểm tra tính đối xứng
    res = f(n)
    return is_palindrome(str(res))

if __name__ == "__main__":
    print("--- ĐẠI HỘI CHIÊU THỨC L08: FUNCTIONS AS OBJECTS ---")
    
    # Thử lửa chiêu thức same_chars
    test_cases = [
        ("abc", "cab", True),
        ("abccc", "caaab", True),
        ("abcd", "cabaa", False),
        ("abcabc", "cabz", False)
    ]
    
    for s1, s2, expected in test_cases:
        result = same_chars(s1, s2)
        status = "✅ ĐẮC ĐẠO" if result == expected else "❌ TẨU HỎA"
        print(f"same_chars('{s1}', '{s2}') -> {result} ({status})")
    
    print("\n--- THỬ LỬA ĐỆ QUY & HÀM BẬC CAO ---")
    # Thử lửa f_yields_palindrome
    def f_plus_1(x): return x + 1
    def f_double(x): return x * 2
    
    print(f"f_yields_palindrome(2, f_plus_1) -> {f_yields_palindrome(2, f_plus_1)} (Expected: True)")
    print(f"f_yields_palindrome(76, f_plus_1) -> {f_yields_palindrome(76, f_plus_1)} (Expected: True)")
    print(f"f_yields_palindrome(11, f_double) -> {f_yields_palindrome(11, f_double)} (Expected: True)")
    print(f"f_yields_palindrome(123, f_double) -> {f_yields_palindrome(123, f_double)} (Expected: False)")
    
    print("-" * 40)
