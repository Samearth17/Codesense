from cryptography.fernet import Fernet
import base64

def encrypt(message):
 key = Fernet.generate_key() 
 cipher_suite = Fernet(key)
 cipher_text = cipher_suite.encrypt(message) 
 cipher_text_string = str(cipher_text, 'utf-8')
 encoded_text = base64.b64encode(key)
 return cipher_text_string, encoded_text

def decrypt(cipher_text_string, encoded_text):
 key = base64.b64decode(encoded_text)
 cipher_suite = Fernet(key)
 plain_text = cipher_suite.decrypt(cipher_text_string) 
 return plain_text