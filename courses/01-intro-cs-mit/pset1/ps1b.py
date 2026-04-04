## 6.100A PSet 1: Part B
## Name:
## Time Spent:
## Collaborators:

##########################################################################################
## Get user input for yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise below ##
##########################################################################################
yearly_salary = float(input("Enter your starting yearly salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
cost_of_dream_home = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter the semi-annual raise, as a decimal: "))

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
    # Lợi nhuận đầu tư dựa trên số tiền đầu tháng
    current_savings += current_savings * (r / 12)
    # Tiết kiệm từ lương tháng
    current_savings += (yearly_salary / 12) * portion_saved
    
    months += 1
    
    # Tăng lương mỗi 6 tháng (ở cuối tháng thứ 6, 12, 18, ...)
    if months % 6 == 0:
        yearly_salary += yearly_salary * semi_annual_raise

print(f"Number of months: {months}")

