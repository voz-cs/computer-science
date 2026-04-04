## MIT 6.100L Lecture 4: Loops over Strings, Guess-and-Check, Binary - Finger Exercise
## Task: 
## Assume you are given a positive integer variable named N. 
## Write a piece of Python code that finds the cube root of N. 
## The code prints the cube root if N is a perfect cube or it prints error if N is not a perfect cube. 
## Hint: use a loop that increments a counter—you decide when the counter should stop.

# Giả sử N là một số nguyên dương. Gán thử giá trị để test:
# Ví dụ: N = 27 (căn bậc 3 là 3), N = 28 (không phải lập phương hoàn hảo)
N = 27

guess = 3

# Sử dụng thuật toán Guess-and-Check (Liệt kê cạn kiệt)
while guess**3 < N:
    guess += 1

if guess**3 == N:
    print(guess)
else:
    print("error")
