# install the module 
# in command prompt
pip install googletrans

# import module
from googletrans import Translator

# create an object
translator = Translator()

# define text
text = "Hello, this is a sample text to translate."

# call the function and pass the text
translation = translator.translate(text, dest='fr') 

# print the translation 
print(translation.text)