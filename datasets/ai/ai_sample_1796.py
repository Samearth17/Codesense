contactlist = {}

# Function to add contact
def add_contact():
  name = input("Enter the name of the contact: ")
  phone = input("Enter the phone number: ")
  email = input("Enter the email address: ")

  contactlist[name] = {
    "Phone": phone,
    "Email": email
  }
  print("Contact saved successfully!")

# Function to update contact
def update_contact():
  name = input("Enter the name of the contact: ")
  if name in contactlist:
    phone = input("Enter the new phone number: ")
    email = input("Enter the new email address: ")

    contactlist[name]["Phone"] = phone
    contactlist[name]["Email"] = email
    print("Contact updated successfully!")
  else:
    print("Contact not found!")

# Main program
while(1):
  print("1. Add contact")
  print("2. Update contact")
  print("3. Exit")

  option = int(input("Enter your choice: "))

  if option == 1:
    add_contact()
  elif option == 2:
    update_contact()
  else:
    break