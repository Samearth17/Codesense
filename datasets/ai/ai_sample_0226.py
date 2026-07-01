def calculator():
  while True:
    try:
      userInput = input('Input equation (type "quit" to exit): ')

      if userInput == "quit":
        break
        
      result = eval(userInput)
      print(result)

    except:
      print('Invalid equation')

calculator()