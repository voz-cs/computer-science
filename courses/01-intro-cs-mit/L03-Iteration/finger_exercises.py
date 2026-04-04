## MIT 6.100L Lecture 3: Iteration - Finger Exercise
## Task: 
## Assume you are given a positive integer variable named N. 
## Write a piece of Python code that prints hello world on separate lines, N times. 
## You can use either a while loop or a for loop.

# Giả sử N là một số nguyên dương. Gán thử giá trị để test:
N = 10

print("--- Sử dụng vòng lặp for ---")
for i in range(N):
    print("hello world")

print("\n--- Sử dụng vòng lặp while ---")
count = 0
while count < N:
    print("hello world")
    count += 1
