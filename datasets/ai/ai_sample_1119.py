# Import relevant libraries
import tkinter as tk 
import hashlib

# Create the main window 
root = tk.Tk()
root.title('Password Manager')

# Create a secure password database
password_storage = {}

# Create a function for hashing the password
def hash_password(password):
  hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()
  return hashed_password

# Create an authentication system to prompt the user to enter a username and password
def authenticate():
  username_entry = tk.Entry(root) 
  username_entry.pack()

  password_entry = tk.Entry(root, show="*") 
  password_entry.pack()

  def authenticate_user():
    username = username_entry.get()
    password = password_entry.get()
    hashed_password = hash_password(password)
    if username in password_storage and password_storage[username] == hashed_password:
      print('Authenticated!')
    else:
      print('Incorrect')
  tk.Button(root, text='Authenticate', command=authenticate_user).pack()

# Call the authenticate function
authenticate()

root.mainloop()