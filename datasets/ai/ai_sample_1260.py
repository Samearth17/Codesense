import io
import os

# Imports the Google Cloud client library
from google.cloud import vision

# Instantiates a client
client = vision.ImageAnnotatorClient()

# The name of the image file to annotate
file_name = 'park.jpg'

# Loads the image
with io.open(file_name, 'rb') as image_file:
 content = image_file.read()

image = vision.types.Image(content=content)

# Performs label detection on the image file
response = client.label_detection(image=image)
labels = response.label_annotations

print('Labels:')
for label in labels:
 print(label.description)

# Performs object detection
response = client.object_localization(image=image)
objects = response.localized_object_annotations

print('Objects:')
for object_ in objects:
 print(object_.name)