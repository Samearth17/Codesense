from google.cloud import texttospeech

# Create a client
client = texttospeech.TextToSpeechClient()

# Construct the request
text = 'Hello World!'
synthesis_input = texttospeech.types.SynthesisInput(text=text)
voice = texttospeech.types.VoiceSelectionParams(
 language_code='en-US',
 ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

# Select the type of audio file you want returned
audio_config = texttospeech.types.AudioConfig(
 audio_encoding=texttospeech.enums.AudioEncoding.MP3)

# Perform the text-to-speech request
response = client.synthesize_speech(synthesis_input, voice, audio_config)

# Write the response to an audio file
with open('output.mp3', 'wb') as out:
 out.write(response.audio_content)
 print('Audio content written to file "output.mp3"')