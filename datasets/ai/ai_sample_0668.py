def encode_caesar_cipher(string, key):
 # initialize an empty result string
 result_string = ''
 
 # loop through the characters in the string
 for char in string:
 # get the ASCII value of the character
 ascii_value = ord(char)
 
 # do the encryption
 if (ascii_value >= 65 and ascii_value <= 90): # uppercase alphabet
 ascii_value += key
 if (ascii_value > 90):
 ascii_value -= 26
 elif (ascii_value >= 97 and ascii_value <= 122): #lowercase alphabet
 ascii_value += key
 if (ascii_value > 122):
 ascii_value -= 26 
 
 # add the encrypted character to the result string
 result_string += chr(ascii_value)
 
 return result_string
 
 
encoded_string = encode_caesar_cipher(string, key)
print(encoded_string)
# prints Jgnnq Yqtnf