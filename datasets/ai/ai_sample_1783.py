def caesar_cipher(message, shift):
    encoded_msg = ""
    for char in message:
        if char.isalpha():
            char_code = ord(char)
            char_code += shift
            if char.isupper():
                if char_code > ord('Z'):
                    char_code -= 26
                elif char_code < ord('A'):
                    char_code += 26
            elif char.islower():
                if char_code > ord('z'):
                    char_code -= 26
                elif char_code < ord('a'):
                    char_code += 26
            encoded_msg += chr(char_code)
        else:
            encoded_msg += char
    return encoded_msg

message = "hello world"
shift = 3
encoded_msg = caesar_cipher(message, shift)
print("Encoded message:", encoded_msg) # -> Encoded message: khoor zruog