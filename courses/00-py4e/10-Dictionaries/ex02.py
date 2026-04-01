"""
Exercise 2: Write a program that categorizes each mail message by which day 
of the week the commit was done. To do this look for lines that start with 
“From”, then look for the third word and keep a running count of each of 
the days of the week. At the end of the program print out the contents of 
your dictionary (order does not matter).
"""
# Exercise 2: Categorize mail by day of week


fname = input('Enter a file name: ')
if len(fname) < 1: fname = 'mbox-short.txt'

try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()

counts = dict()
for line in fhand:
    # Use guardian pattern (only process "From " lines)
    if not line.startswith('From '): continue
    
    words = line.split()
    if len(words) < 3: continue
    
    # Day is the 3rd word
    day = words[2]
    counts[day] = counts.get(day, 0) + 1

print(counts)
