# Exercise 1: Finding the most active committer
# Requirement: Read mbox-short.txt, count messages by person using a dictionary,
# then use a list of (count, email) tuples to find the top committer.

import os

def solve():
    fname = "mbox-short.txt"
    if not os.path.exists(fname):
        print(f"File {fname} not found!")
        return

    counts = dict()
    try:
        with open(fname) as f:
            for line in f:
                if not line.startswith("From "): continue
                words = line.split()
                if len(words) < 2: continue
                email = words[1]
                counts[email] = counts.get(email, 0) + 1
    except Exception as e:
        print(f"Lỗi đọc file: {e}")
        return

    # MINDSET: Tạo list các tuple (count, email) để sort theo số lượng
    lst = list()
    for email, count in counts.items():
        lst.append((count, email))

    # Sort giảm dần (reverse=True)
    lst.sort(reverse=True)

    # Lấy người đầu tiên (người có count cao nhất)
    if len(lst) > 0:
        count, email = lst[0]
        print(f"Thiện xạ nhất: {email} với {count} commits")
    else:
        print("Không tìm thấy dữ liệu phù hợp.")

if __name__ == "__main__":
    solve()
