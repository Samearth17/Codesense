import sys

def factorial(n):
 if n == 1 or n == 0:
 return 1
 else:
 return n * factorial(n-1)

if __name__ == '__main__':
 if len(sys.argv) > 1 and sys.argv[1] == '--number':
 try:
 number = int(input('Please enter a number: '))
 print(f'{number}! = {factorial(number)}')
 except ValueError:
 print('Please enter a valid number.')
else:
 print('Please provide a single argument --number')