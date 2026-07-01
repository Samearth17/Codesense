def print_menu():
  print('1. Find the square ')
  print('2. Find the cube ')
  print('3. Quit')
  print()

#Take Input from the user 
choice = int(input("Enter your choice: "))
while choice != 3: 
  if choice==1: 
    num = int(input("Enter a number: "))
    print("The square of",num,"is",num*num)
  elif choice==2: 
    num = int(input("Enter a number: ")) 
    print("The cube of",num,"is",num**3) 
  elif choice==3: 
    print("Bye!")
  else: 
    print("Sorry, wrong input")
  print() 
  choice = int(input("Enter your choice: ")) 
print("Bye!")