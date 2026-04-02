# MIT 6.100L Lecture 2 Finger Exercises

"""
Exercise: 
1. Ask the user for a number (Remember: input() returns a string).
2. Print "positive" if number is greater than 0.
3. Print "negative" if number is less than 0.
4. Print "zero" if number is equal to 0.
"""

def exercise_1():
    # TODO: Nhận input từ người dùng
    user_input = input("Nhập một con số: ")
    
    # Ép kiểu từ string sang int (hoặc float)
    try:
        num = float(user_input)
    except ValueError:
        print("Lỗi: Vui lòng nhập một con số hợp lệ.")
        return

    # TODO: Thực hiện Logic Rẽ nhánh (Branching)
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("zero")

if __name__ == "__main__":
    exercise_1()
