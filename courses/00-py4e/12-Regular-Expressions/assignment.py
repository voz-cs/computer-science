import re

def solve():
    # Mở file dữ liệu thực tế
    try:
        fhand = open("regex_sum_1687753.txt")
    except FileNotFoundError:
        print("Không tìm thấy file regex_sum_1687753.txt. Vui lòng kiểm tra lại.")
        return

    total = 0
    count = 0
    
    # Duyệt từng dòng trong file
    for line in fhand:
        # Tìm tất cả các chuỗi chữ số [0-9]+
        numbers = re.findall('[0-9]+', line)
        for num in numbers:
            total += int(num)
            count += 1
            
    print(f"Số lượng con số tìm thấy: {count}")
    print(f"Tổng các con số là: {total}")

if __name__ == "__main__":
    solve()
