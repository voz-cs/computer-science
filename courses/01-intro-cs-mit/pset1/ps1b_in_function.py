def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
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
	    current_savings += current_savings * (r / 12)
	    # Monthly salary savings
	    current_savings += (yearly_salary / 12) * portion_saved
	    
	    months += 1
	    
	    # Increase salary every 6 months (at the end of months 6, 12, 18, ...)
	    if months % 6 == 0:
	        yearly_salary += yearly_salary * semi_annual_raise
	
	print(f"Number of months: {months}")
	
	return months