def part_a(yearly_salary, portion_saved, cost_of_dream_home):
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
	    # Monthly investment return based on beginning of month balance
	    monthly_return = current_savings * (r / 12)
	    # Monthly savings from salary
	    monthly_savings = (yearly_salary / 12) * portion_saved
	    
	    # Update total savings
	    current_savings += monthly_return + monthly_savings
	    months += 1
	
	print(f"Number of months: {months}")
	return months