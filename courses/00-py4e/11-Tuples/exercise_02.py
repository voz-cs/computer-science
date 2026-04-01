# Exercise 2: Hour Distribution
def solve():
    fhand = open("mbox-short.txt")
    counts = {}
    for line in fhand:
        if not line.startswith("From "): continue
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        counts[hour] = counts.get(hour, 0) + 1

    for hour, count in sorted(counts.items()):
        print(hour, count)

if __name__ == "__main__":
    solve()
