"""
Exercise 1: Download a copy of the file www.py4e.com/code3/words.txt
Write a program that reads the words in words.txt and stores them as keys 
in a dictionary. It doesn’t matter what the values are. Then you can use 
the 'in' operator as a fast way to check whether a string is in the dictionary.
"""
# Exercise 1: Fast word lookup


fname = 'words.txt'
fhand = open(fname)

words_dict = dict()
for line in fhand:
    words = line.split()
    for word in words:
        words_dict[word] = None # Value doesn't matter

# Test lookup
test_word = 'writing'
if test_word in words_dict:
    print(f"'{test_word}' is in the dictionary")
else:
    print(f"'{test_word}' is NOT in the dictionary")
