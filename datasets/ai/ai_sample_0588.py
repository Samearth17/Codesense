# import the necessary packages
import pygame
import requests
from gtts import gTTS

# define an API call to scrape website text
url = 'example.com'
content = requests.get(url).text

# initialize the pygame module
pygame.mixer.init()

# generate the text-to-speech audio
tts = gTTS(content)

# save the text-to-speech audio
tts.save('text.mp3')

# play the audio
pygame.mixer.music.load('text.mp3')
pygame.mixer.music.play()

# wait for the audio to finish
while pygame.mixer.music.get_busy(): 
    pygame.time.Clock().tick(10)