import hashlib

class User:
    def __init__(self, username, password):
        self.username = username
        self.password_hash = self.hash_password(password)

    def check_password(self, password):
        if self.hash_password(password) == self.password_hash:
            return True
        else:
            return False

    def hash_password(self, password):
        return hashlib.sha256(password.encode('utf-8')).hexdigest()

users = {}

def register(username, password):
    if username in users:
        print('Username already exists!')
        return
    
    users[username] = User(username, password)
    print('Registration successful!')
    
def login(username, password):
    if username not in users:
        print('Username doesn\'t exist!')
        return 
    
    user = users[username]
    if user.check_password(password):
        print('Login successful!')
    else:
        print('Wrong password!')