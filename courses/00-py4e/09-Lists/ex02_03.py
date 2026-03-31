# Exercise 2 & 3: Guardian logic refinement
# Exercise 2: Figure out which line is not properly guarded.
# Exercise 3: Rewrite with a compound logical expression using 'or'.

fhand = open('mbox-short.txt')

count = 0
for line in fhand:
    words = line.split()
    # Exercise 3: Compound guard
    # The line "if words[0] != 'From'" is dangerous if there are NO words.
    # The line "print(words[2])" is dangerous if there are FEWER than 3 words.
    
    # Combined guard:
    if len(words) < 3 or words[0] != 'From':
        continue
    
    print(words[2])
