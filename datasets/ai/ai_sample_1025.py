import os

def detect_coronavirus(input_dir):
    # input_dir - The directory containing the text documents
    total_occurrences = 0

    # Iterate through each file in the input_dir
    for file in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file)

        # Read the file
        with open(file_path, 'r') as f:
            data = f.read()

            # Detect the occurrences of the word "coronavirus"
            occurrence_count = data.lower().count("coronavirus")
            total_occurrences += occurrence_count

    return total_occurrences

# Call the function
occurrences = detect_coronavirus('input_dir')
print(f'The word "coronavirus" has occurred {occurrences} times.')