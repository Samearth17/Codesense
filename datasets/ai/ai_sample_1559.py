def pascal_triangle(n): 
	
	# 1st base case 
	if n == 0: 
		return [] 
	elif n == 1: 
		return [[1]]
	  
	# 2nd base case 
	else: 
		new_row = [1] 
		result = pascal_triangle(n-1) 
		previous_row = result[-1] 

		# making the current row 
		for i in range(len(previous_row)-1): 
			value = previous_row[i] + previous_row[i+1] 
			new_row.append(value) 

		new_row += [1] 
		result.append(new_row) 
		
	return result