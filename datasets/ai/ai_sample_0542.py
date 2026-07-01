import base64
from Crypto.Cipher import AES

def encrypt_string(plain_text, key, iv):
 # convert strings to bytes
 plain_text_bytestring = bytes(plain_text, encoding='utf8')
 key = bytes(key, encoding='utf8')
 iv = bytes(iv, encoding='utf8')

 # create an AES cipher object with the key
 cipher = AES.new(key, AES.MODE_CBC, iv)

 # encrypt the message using the cipher object
 encrypted_string = cipher.encrypt(plain_text_bytestring)

 # base64 encode the encrypted message
 base64_encrypted_string = base64.b64encode(encrypted_string)

 # return the base64 encoded message
 return base64_encrypted_string.decode('utf-8')

def decrypt_string(base64_encrypted_string, key, iv):
 # convert strings to bytes
 base64_encrypted_string = bytes(base64_encrypted_string, encoding='utf8')
 key = bytes(key, encoding='utf8')
 iv = bytes(iv, encoding='utf8')

 # decode the base encoded message
 encrypted_string = base64.b64decode(base64_encrypted_string)

 # create an AES cipher object with the key
 cipher = AES.new(key, AES.MODE_CBC, iv)

 # decrypt the message using the cipher object
 decrypted_string = cipher.decrypt(encrypted_string)

 # return the decrypted message in string format
 return decrypted_string.decode('utf-8')