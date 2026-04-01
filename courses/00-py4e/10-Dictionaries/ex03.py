"""
Exercise 3: Write a program to read through a mail log, build a histogram 
using a dictionary to count how many messages have come from each email 
address, and print the dictionary.
"""
# Exercise 3: Email address histogram


fname = input('Enter a file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    if not line.startswith('From '): continue
    
    words = line.split()
    if len(words) < 2: continue
    
    email = words[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)
