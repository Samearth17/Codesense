def encrypt(string, shift):
    encrypted_string = ""
 
    for char in string:
        if char == ' ':
            encrypted_string += char
        else:
            encrypted_ascii = ord(char) + shift
            if encrypted_ascii > ord('z'):
                encrypted_ascii -= 26
            encrypted_string += chr(encrypted_ascii)
 
    return encrypted_string

def decrypt(encrypted_string, shift):
    decrypted_string = ""
 
    for char in encrypted_string:
        if char == ' ':
            decrypted_string += char
        else:
            decrypted_ascii = ord(char) - shift
            if decrypted_ascii < ord('a'):
                decrypted_ascii += 26
            decrypted_string += chr(decrypted_ascii)
    return decrypted_string