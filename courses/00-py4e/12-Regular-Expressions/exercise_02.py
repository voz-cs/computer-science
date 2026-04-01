# Exercise 02: Extract Revision Numbers and calculate Average
import re

def solve():
    fhand = open("mbox-short.txt")
    nums = []
    for line in fhand:
        line = line.rstrip()
        x = re.findall('^New Revision: ([0-9]+)', line)
        if len(x) > 0:
            nums.append(int(x[0]))
    
    if len(nums) > 0:
        print(int(sum(nums) / len(nums)))

if __name__ == "__main__":
    solve()
