def nth_prime(n):
  
 num_primes = 0
 curr_num = 2
 
 while num_primes < n:
   is_prime = True
   for i in range(2, curr_num):
       if curr_num % i == 0:
           is_prime = False
           break
   if is_prime:
       num_primes += 1
   curr_num += 1

return curr_num - 1