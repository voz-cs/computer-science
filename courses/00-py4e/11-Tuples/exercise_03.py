# Exercise 3: Letter Frequency
# Requirement: Count frequency of letters (a-z) in a file and print in decreasing order.

import string
import os

def solve():
    fname = "romeo.txt" # or any text file
    if not os.path.exists(fname):
        print(f"File {fname} not found!")
        return

    counts = dict()
    try:
        with open(fname) as f:
            for line in f:
                line = line.lower()
                # Loại bỏ dấu câu và ký tự không phải chữ cái
                line = line.translate(line.maketrans('', '', string.punctuation + string.digits + " \n\r\t"))
                for char in line:
                    counts[char] = counts.get(char, 0) + 1
    except Exception as e:
        print(f"Lỗi: {e}")
        return

    # MINDSET: Chuyển sang (count, char) để sort theo số lượng giảm dần
    lst = list()
    for char, count in counts.items():
        lst.append((count, char))

    lst.sort(reverse=True)

    for count, char in lst:
        print(f"'{char}': {count}")

if __name__ == "__main__":
    solve()
