## 6.100A PSet 1: Part C
## Name:
## Time Spent:
## Collaborators:

##############################################
## Get user input for initial_deposit below ##
##############################################
initial_deposit = float(input("Enter the initial deposit: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
cost_of_dream_home = 800000
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
months = 36
epsilon = 100

steps = 0
r = None

# Bisection search parameters
low = 0
high = 10000 # 10000 đại diện cho 100% (1.0) 

##################################################################################################
## Determine the lowest rate of return needed to get the down payment for your dream home below ##
##################################################################################################
# Kiểm tra xem có thể đạt mục tiêu với lãi suất tối đa (100%) không
if initial_deposit * (1 + 1.0/12)**months < down_payment - epsilon:
    r = None
    steps = 0
# Kiểm tra xem có cần lãi suất không (nếu tiền gửi đã đủ)
elif initial_deposit >= down_payment - epsilon:
    r = 0.0
    steps = 0
else:
    while low <= high:
        steps += 1
        guess = (low + high) // 2
        r_guess = guess / 10000.0
        
        # Công thức tính lợi nhuận gộp từ khoản gửi ban đầu
        amount_saved = initial_deposit * (1 + r_guess / 12)**months
        
        if abs(amount_saved - down_payment) < epsilon:
            r = r_guess
            break
        elif amount_saved < down_payment:
            low = guess + 1
        else:
            high = guess - 1
            r = r_guess # Lưu lại giá trị khả thi nhất nếu epsilon chưa đạt

print(f"Best savings rate: {r}")
print(f"Steps in bisection search: {steps}")

