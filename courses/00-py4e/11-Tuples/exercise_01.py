# Exercise 1: Most active committer
def solve():
    fhand = open("mbox-short.txt")
    counts = {}
    for line in fhand:
        if not line.startswith("From "): continue
        words = line.split()
        email = words[1]
        counts[email] = counts.get(email, 0) + 1

    # DSU Pattern: Decorate, Sort, Undecorate
    lst = []
    for email, count in counts.items():
        lst.append((count, email))

    lst.sort(reverse=True)

    for count, email in lst[:1]:
        print(email, count)

if __name__ == "__main__":
    solve()
