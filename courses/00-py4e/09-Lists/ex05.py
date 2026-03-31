# Exercise 5: Minimalist Email Client

fname = input("Enter a file name: ")
if len(fname) < 1: fname = "mbox-short.txt"

try:
    fhand = open(fname)
except FileNotFoundError:
    print(f"Error: File {fname} not found.")
    quit()

count = 0
for line in fhand:
    # Look for lines that start with "From " (not "From:")
    if not line.startswith('From '): continue
    
    # Split the line into words
    words = line.split()
    
    # The sender is the 2nd word
    if len(words) >= 2:
        print(words[1])
        count += 1

print(f"There were {count} lines in the file with From as the first word")
