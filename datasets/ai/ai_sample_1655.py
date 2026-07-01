def Fibonacci_Series(num):

  i = 0
  First_Value = 0
  Second_Value = 1
   
  if num < 0:
   print("Incorrect input")
  elif num == 0:
   print(First_Value)
  elif num == 1:
   print(First_Value,",",Second_Value,end=" , ")
  else:
   print(First_Value,",",Second_Value,end=" , ")
   while i < num-2:
       next_Value = First_Value + Second_Value
       print(next_Value,end=" , ")
       First_Value = Second_Value
       Second_Value = next_Value
       i = i + 1

num = 50
Fibonacci_Series(num)