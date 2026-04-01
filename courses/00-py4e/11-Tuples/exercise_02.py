# Exercise 2: Hour Distribution
# Requirement: Pull the hour from the 'From ' line, count frequency,
# then print sorted by hour (00, 01, 02...).

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
                if len(words) < 6: continue
                # format: From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
                # words[5] is the time "09:14:16"
                time = words[5]
                hour = time.split(":")[0]
                counts[hour] = counts.get(hour, 0) + 1
    except Exception as e:
        print(f"Lỗi: {e}")
        return

    # MINDSET: sort theo hour (key)
    # sorted(counts.items()) sẽ tự động sort theo phần tử đầu tiên của Tuple (hour)
    for hour, count in sorted(counts.items()):
        print(hour, count)

if __name__ == "__main__":
    solve()
