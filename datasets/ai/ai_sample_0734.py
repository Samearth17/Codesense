#Python code for subtracting two 8-bit integers

# Function to subtract two 8-bit binary numbers 
# a and b 
def subtractTwoBits(a, b): 
	# a is larger 
	if (a >= b): 
		
		# Array storing values 
		# after X-OR 
		diff = [0] * 8
		
		# Till same bits reach 
		for i in range(8): 
			
			# If current of b is 0 
			if (b % 2 == 0): 
			
				# Take X-OR with 0 
				diff[i] = (int)(a % 2) 
			
			# If current of b is 1 
			else: 
			
				# Take the X-OR with 1 
				diff[i] = (int)(a % 2) ^ 1
			
			# Right shift 
			a = int(a / 2) 
			b = int(b / 2) 
		
		# Convert the Binary result to Integer 
		return diffToDecimal(diff) 
	
	else: 
		print("Error: a is smaller") 
		return -1

# Function to convert 8 bit 
# binary number to Decimal 
def diffToDecimal(diff): 
	
	# Initialize the value 
	val = 0
	
	# value before raising it  
	# to the power of 2 
	p = 1
	
	# Calculating the decimal value 
	for i in range (7, -1, -1): 
	
		# Subtracting the value 
		val = (val + (diff[i] * p))	 
		p = p * 2
		
	return val 
	
# Driver Code 
x = 15
y = 6
res = subtractTwoBits(x, y) 
print(res)