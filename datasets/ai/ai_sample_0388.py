import bcrypt

def checkPassword(hashed_password):
 # Hash the password
 password = bcrypt.hashpw(password, bcrypt.gensalt()) 

 # Check the password against the hash
 if bcrypt.checkpw(password, hashed_password):
   return True
 else:
   return False

if __name__ == "__main__":
 hashed_password = "abcdefg12345678"
 if checkPassword(hashed_password):
   print("Password match")
 else:
   print("Password verficiation failed")