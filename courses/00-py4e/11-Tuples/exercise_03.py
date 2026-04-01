# Exercise 3: Letter Frequency
import string

def solve():
    fhand = open("romeo.txt")
    counts = {}
    for line in fhand:
        line = line.lower()
        for char in line:
            if char.isalpha():
                counts[char] = counts.get(char, 0) + 1

    lst = []
    for char, count in counts.items():
        lst.append((count, char))

    lst.sort(reverse=True)

    for count, char in lst:
        print(char, count)

if __name__ == "__main__":
    solve()
