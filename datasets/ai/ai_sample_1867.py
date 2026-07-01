def product_without_mul(x, y): 
 result = 0
 while (y > 0): 
    partial_result = 0
    for i in range(y): 
        partial_result += x
    result += partial_result
    y -= 1
   
return result 

x = 3
y = 7

print("Product of two numbers without using 
multiplication operator is ", product_without_mul(x, y))