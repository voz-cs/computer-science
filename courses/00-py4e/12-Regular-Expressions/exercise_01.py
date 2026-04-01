# Exercise 01: Linux grep simulation
import re

def solve():
    regex = input("Nhập biểu thức chính quy (regular expression): ")
    try:
        fhand = open("mbox-short.txt")
    except FileNotFoundError:
        print("Không tìm thấy file mbox-short.txt.")
        return

    count = 0
    for line in fhand:
        line = line.rstrip()
        if re.search(regex, line):
            count += 1
    print(f"mbox-short.txt có {count} dòng khớp với {regex}")

if __name__ == "__main__":
    solve()
