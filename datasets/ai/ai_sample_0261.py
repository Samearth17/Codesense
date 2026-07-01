class Contact:
    def __init__(self, single_name, last_name, email, address, phone_number):
        """
        This is the constructor for the contact class.
        """
        self.single_name = single_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone_number = phone_number

    def get_full_name(self):
        """
        This method returns the full name of the contact.
        """
        return self.last_name + ", " + self.single_name

    def get_email(self):
        """
        This method returns the email of the contact.
        """
        return self.email

    def get_address(self):
        """
       This method returns the address of the contact.
        """
        return self.address

    def get_phone_number(self):
        """
        This method returns the phone number of the contact.
        """
        return self.phone_number