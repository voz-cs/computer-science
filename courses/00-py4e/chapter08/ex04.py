# Exercise 4: Find all unique words in a file

fname = input("Enter file: ")
if len(fname) < 1: fname = "romeo.txt"

try:
    fhand = open(fname)
except FileNotFoundError:
    print(f"Error: File {fname} not found.")
    quit()

# Read the file line by line
for line in fhand:
    # Split each line into a list of words
    words = line.split()
    
    # Check each word and add it to unique_words if not already present
    for word in words:
        if word not in unique_words:
            unique_words.append(word)

# Sort the final list alphabetically
unique_words.sort()

# Print the result
print(unique_words)
