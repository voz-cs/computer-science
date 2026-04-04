## 6.100A PSet 1: Part A
## Name:
## Time Spent:
## Collaborators: 

##################################################################################
## Get user input for yearly_salary, portion_saved and cost_of_dream_home below ##
##################################################################################
yearly_salary = float(input("Enter your yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))

#########################################################################
## Initialize other variables you need (if any) for your program below ##
#########################################################################
portion_down_payment = 0.25
down_payment = cost_of_dream_home * portion_down_payment
current_savings = 0.0
r = 0.05
months = 0

###############################################################################################
## Determine how many months it would take to get the down payment for your dream home below ## 
###############################################################################################
while current_savings < down_payment:
    # Tính lợi nhuận đầu tư hàng tháng dựa trên số dư đầu tháng
    monthly_return = current_savings * (r / 12)
    # Tính số tiền tiết kiệm từ lương hàng tháng
    monthly_savings = (yearly_salary / 12) * portion_saved
    
    # Cập nhật tổng số tiền tiết kiệm
    current_savings += monthly_return + monthly_savings
    months += 1

print(f"Number of months: {months}")
