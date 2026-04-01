"""
Exercise 4: Add code to the previous program to figure out who has the 
most messages in the file. After all the data has been read and the 
dictionary has been created, look through the dictionary using a maximum 
loop (see Chapter 5: Maximum and minimum loops) to find who has the most 
messages and print how many messages the person has.
"""
# Exercise 4: Find sender with most messages


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

# Finding the maximum sender manually (as requested by Chapter 5 logic)
max_email = None
max_count = None

for email, count in counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

print(f"{max_email} {max_count}")
