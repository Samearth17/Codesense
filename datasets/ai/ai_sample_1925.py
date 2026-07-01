def pattern(n):
 m = 0
 for i in range(1, n+1):
 for j in range(1, m+1):
 print("*", end="")
 m = m + 2
 
 for k in range(1, n-i+1):
 print("#", end="")
 print()

pattern(5) 
/* Output: 
*#*#*
**#**
***#
****
*/