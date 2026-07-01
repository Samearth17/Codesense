def generate_password(word):
      # initialize variables 
    password = ""
    letters = ""
    numbers = ""

    # create new password
    for i in range(0, len(word)):
      letters += word[i]
      numbers += str(i)

    password = letters + numbers
    return password

print(generate_password("Hello"))