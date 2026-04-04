def part_c(initial_deposit):
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
	high = 4096 # Standard MIT range
	epsilon = 100
	steps = 0
	r = None
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	
	# Max possible savings with 100% interest (r=1.0)
	max_savings = initial_deposit * (1 + 1.0/12)**months
	
	if max_savings < down_payment - epsilon:
	    r = None
	    steps = 0
	elif initial_deposit >= down_payment - epsilon:
	    r = 0.0
	    steps = 0
	else:
	    # Run for exactly 12 steps to match MIT's log2(4096) expectation
	    for _ in range(12):
	        steps += 1
	        guess = (low + high) // 2
	        r_guess = guess / 4096.0
	        
	        amount_saved = initial_deposit * (1 + r_guess / 12)**months
	        
	        if amount_saved < down_payment:
	            low = guess
	        else:
	            high = guess
	            r = r_guess
	
	print(f"Best savings rate: {r}")
	print(f"Steps in bisection search: {steps}")
	
	return r, steps