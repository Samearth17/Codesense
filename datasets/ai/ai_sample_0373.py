import hashlib 
  
def encrypt_string(string, password):
    md5_string = hashlib.md5(string.encode()).hexdigest()
    password_string = hashlib.md5(password.encode()).hexdigest()
    result = ""

    for i in range(32):
        result += md5_string[i] + password_string[i]
    return result

string = "Hello World!"
password = "password"

result = encrypt_string(string, password)
print(result)