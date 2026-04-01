"""
Exercise 5: This program records the domain name (instead of the address) 
where the message was sent from instead of who the mail came from 
(i.e., the whole email address). At the end of the program, print out 
the contents of your dictionary.
"""
# Exercise 5: Email domain histogram


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
    # Split the email by '@' to get the domain
    at_pos = email.find('@')
    domain = email[at_pos+1:]
    
    counts[domain] = counts.get(domain, 0) + 1

print(counts)
