def decrypt(message, key):
    decrypted_message = ""
    
    for char in message:
        ascii_value = ord(char)
        decrypted_char = chr(ascii_value - key)
        decrypted_message += decrypted_char
    
    return decrypted_message

message = "AB cDE@5sfg90~!"
key = 6

decrypted_message = decrypt(message, key)
print(decrypted_message)