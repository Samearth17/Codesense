# import the required libraries 
import base64 
from cryptography.hazmat.backends import default_backend 
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC 
  
# message to be encrypted 
message = "This is an example" 
  
# encode the message in UTF-8 format 
encoded_message = message.encode('utf-8') 
  
# generate a random salt 
salt = os.urandom(16) 
  
# derive an encryption key from the message, 
# salt and number of iterations 
kdf = PBKDF2HMAC( 
    algorithm=hashes.SHA256(), 
    length=32, 
    salt=salt, 
    iterations=100000, 
    backend=default_backend() 
) 
key = base64.urlsafe_b64encode(kdf.derive(message)) 
  
# encode the message 
encoded_message = base64.b64encode(message.encode('utf-8')) 
  
# encrypt the message  
encrypter = Cipher(algorithms.AES(key), modes.GCM(salt), backend=default_backend()).encryptor() 
  
# finally calculate the encrypted message 
ct = encrypter.update(encoded_message) + encrypter.finalize() 

print(ct)