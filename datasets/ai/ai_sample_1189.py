#!/usr/bin/env python3

# Addition
if "add" in sys.argv[1]:
 try:
  num1 = int(sys.argv[2])
  num2 = int(sys.argv[3])
  print("Result of", num1, "+", num2, " = ", num1 + num2)
 except ValueError:
  print("Please provide valid input values")

# Subtraction
elif "sub" in sys.argv[1]:
 try:
  num1 = int(sys.argv[2])
  num2 = int(sys.argv[3])
  print("Result of", num1, "-", num2, " = ", num1 - num2)
 except ValueError:
  print("Please provide valid input values")

# Multiplication
elif "mul" in sys.argv[1]:
 try:
  num1 = int(sys.argv[2])
  num2 = int(sys.argv[3])
  print("Result of", num1, "*", num2, " = ", num1 * num2)
 except ValueError:
  print("Please provide valid input values")

# Division
elif "div" in sys.argv[1]:
 try:
  num1 = int(sys.argv[2])
  num2 = int(sys.argv[3])
  print("Result of", num1, "/", num2, " = ", num1 / num2)
 except ValueError:
  print("Please provide valid input values")