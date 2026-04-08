# 📜 Luyện Khí Tầng 07: Tâm Pháp Đóng Gói (Functions)
# Course: MIT 6.100L
# Mục tiêu: Thấu triệt cách xây dựng Hàm, quản lý Scope và Abstraction.

import sys
import io

# Đảm bảo terminal hỗ trợ UTF-8 để hiển thị linh ngữ (Vietnamese)
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def div_by(n, d):
    """
    n và d là số nguyên dương > 0.
    Trả về True nếu d chia hết n, ngược lại False.
    """
    return n % d == 0

def sum_odd(a, b):
    """
    a và b là các số nguyên.
    Tính tổng các số lẻ trong khoảng [a, b] (tính cả a và b).
    """
    total = 0
    for i in range(a, b + 1):
        if i % 2 != 0:
            total += i
    return total

def is_palindrome(s):
    """
    s là một chuỗi (string).
    Trả về True nếu s là chuỗi đối xứng (palindrome), ngược lại False.
    Ví dụ: '222' -> True, 'abc' -> False.
    """
    # Chiêu thức 1: So sánh chuỗi với bản đảo ngược (Slicing)
    # return s == s[::-1]
    
    # Chiêu thức 2: Dùng vòng lặp (Manual check)
    for i in range(len(s)//2):
        if s[i] != s[len(s)-i-1]:
            return False
    return True

def keep_consonants(word):
    """
    word là một chuỗi gồm các chữ cái viết thường.
    Trả về chuỗi chỉ chứa các phụ âm (consonants) theo thứ tự xuất hiện.
    Nguyên âm (vowels): 'aeiou'
    """
    vowels = "aeiou"
    result = ""
    for char in word:
        if char not in vowels:
            result += char
    return result

def first_to_last_diff(s, c):
    """
    s là một chuỗi, c là một ký tự duy nhất.
    Trả về khoảng cách giữa vị trí xuất hiện đầu tiên và cuối cùng của c trong s.
    Nếu c không xuất hiện, trả về -1.
    Ví dụ: ('aaaa', 'a') -> 3, ('abcabc', 'b') -> 3.
    """
    # Chiêu thức: Tìm linh ấn đầu tiên (first) và cuối cùng (last)
    first_idx = -1
    last_idx = -1
    
    for i in range(len(s)):
        if s[i] == c:
            if first_idx == -1:
                first_idx = i
            last_idx = i
            
    if first_idx == -1:
        return -1
    
    return last_idx - first_idx

def test_scope():
    """
    Trận pháp thực nghiệm về Scope (Phạm vi biến).
    """
    x = "Linh lực nội bộ (Local)"
    print(f"Bên trong hàm: x = {x}")

if __name__ == "__main__":
    print("--- ĐẠI HỘI CHIÊU THỨC L07: FUNCTIONS ---")
    
    # Thử lửa bài 1: div_by
    print(f"div_by(10, 3): {div_by(10, 3)}")   # Expected: False
    print(f"div_by(195, 13): {div_by(195, 13)}") # Expected: True
    
    # Thử lửa bài 2: sum_odd
    print(f"sum_odd(2, 4): {sum_odd(2, 4)}") # Expected: 3
    print(f"sum_odd(2, 7): {sum_odd(2, 7)}") # Expected: 3+5+7 = 15
    
    # Thử lửa bài 3: is_palindrome
    print(f"is_palindrome('222'): {is_palindrome('222')}")   # Expected: True
    print(f"is_palindrome('abc'): {is_palindrome('abc')}")   # Expected: False

    # Thử lửa bài 4: keep_consonants
    print(f"keep_consonants('abcd'): {keep_consonants('abcd')}") # Expected: 'bcd'
    print(f"keep_consonants('babas'): {keep_consonants('babas')}") # Expected: 'bbs'

    # Thử lửa bài 5: first_to_last_diff
    print(f"first_to_last_diff('aaaa', 'a'): {first_to_last_diff('aaaa', 'a')}") # Expected: 3
    print(f"first_to_last_diff('abcabcabc', 'b'): {first_to_last_diff('abcabcabc', 'b')}") # Expected: 6
    
    print("-" * 40)
    test_scope()
