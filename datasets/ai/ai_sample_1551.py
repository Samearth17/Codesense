# Library import
import os

# Path of the file
file_name = "myfile.txt"

# Open file
try:
  with open(file_name, 'r') as f:

    # Read file
    contents = f.read()

    # Print file
    print(contents)

except IOError:
  print('Error: file not found!')

finally:
  if f:
    f.close()