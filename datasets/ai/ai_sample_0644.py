def sum_amicable_numbers(start, end):
 amicable_sum = 0
 
 for num in range(start, end + 1):
 divisors = get_divisors(num)
 div_sum = sum(divisors)
 other_divisors = get_divisors(div_sum)
 other_div_sum = sum(other_divisors)
 
 if other_div_sum == num and num != div_sum:
 amicable_sum += num
  
 return amicable_sum
 
 def get_divisors(num):
 divisors = []
 
 for i in range(1, int(num/2) + 1):
 if num % i == 0:
 divisors.append(i)
 
 return divisors

sum_amicable_numbers(1, 10000)