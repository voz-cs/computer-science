# 📜 Luyện Khí Tầng 09: Lambda Functions, Tuples, and Lists
# Course: MIT 6.100L
# Mục tiêu: Thấu triệt Tuples, Lists (Part 1) và tiểu trận pháp Lambda.

import sys
import io

# Đảm bảo terminal hỗ trợ UTF-8 để hiển thị linh ngữ (Vietnamese)
if sys.stdout.encoding != 'utf-8':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def dot_product(tA, tB):
    """
    tA, tB: tuples cùng độ dài.
    Trả về (độ dài, tổng tích cặp).
    """
    # Xác định quy mô của trận pháp (số lượng phần tử)
    length = len(tA)
    
    # Khởi tạo linh đài để tích lũy tổng các tích
    pairwise_sum = 0
    
    # Duyệt qua từng vị trí linh ấn từ 0 đến length-1
    for i in range(length):
        # Nhân linh lực tại cùng vị trí của hai bộ và cộng dồn vào tổng
        pairwise_sum += tA[i] * tB[i]
        
    # Đóng gói quy mô và kết quả cuối cùng vào một Tuple để mang về tàng kinh các
    return (length, pairwise_sum)

def char_counts(s):
    """
    s: chuỗi ký tự thường.
    Trả về (số nguyên âm, số phụ âm).
    """
    vowels = 0
    consonants = 0
    for char in s:
        if char in "aeiou":
            vowels += 1
        else:
            consonants += 1
    return (vowels, consonants)

def sum_and_prod(L):
    """
    L: danh sách số.
    Trả về (tổng, tích).
    """
    total_sum = 0
    total_prod = 1
    for num in L:
        total_sum += num
        total_prod *= num
    return (total_sum, total_prod)

def max_of_both(n, f1, f2):
    """
    n: số nguyên.
    f1, f2: các linh pháp (hàm).
    Trả về giá trị cực đại của f1(i) và f2(i) với 0 <= i <= n.
    """
    max_val = f1(0) # Khởi tại cực hạn ban đầu
    for i in range(n + 1):
        max_val = max(max_val, f1(i), f2(i))
    return max_val

def sublist_sum(L):
    """
    L: danh sách chứa các tiểu danh sách số.
    Trả về tổng của mọi phần tử.
    """
    total = 0
    for subL in L:
        total += sum(subL)
    return total

if __name__ == "__main__":
    print("--- ĐẠI HỘI CHIÊU THỨC L09: TUPLES, LISTS & LAMBDA ---")
    
    # Thử lửa dot_product
    # Khởi tạo hai đạo binh (tuples) để chuẩn bị thử nghiệm
    tA, tB = (1, 2, 3), (4, 5, 6)
    # Triển khai chiêu thức dot_product và thu về kết quả linh diệu
    res = dot_product(tA, tB)
    print(f"dot_product{tA, tB} -> {res} (Expected: (3, 32))")
    
    # Test cases cho các chiêu thức khác
    print(f"char_counts('abcd') -> {char_counts('abcd')} (Expected: (1, 3))")
    print(f"sum_and_prod([1, 2, 3, 4]) -> {sum_and_prod([1, 2, 3, 4])} (Expected: (10, 24))")
    print(f"max_of_both(2, lambda x:x-1, lambda x:x+1) -> {max_of_both(2, lambda x:x-1, lambda x:x+1)} (Expected: 3)")
    print(f"sublist_sum([[1, 2], [4, 5, 6]]) -> {sublist_sum([[1, 2], [4, 5, 6]])} (Expected: 18)")
    
    print("-" * 50)
