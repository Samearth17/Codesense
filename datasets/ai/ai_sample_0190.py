# Python Program to print the Fibonacci series up to n numbers

n = int(input("Enter the value of 'n': "))

# first two numbers
a = 0
b = 1

print("Fibonacci Series:") 
print(a, b, end=" ") 
  
for i in range(2,n):
               
    c = a + b
    a = b
    b = c
    print(c, end = " ")
    
print()