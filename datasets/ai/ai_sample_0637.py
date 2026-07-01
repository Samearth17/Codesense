def find_longest_common_substring(s1, s2):
    # Set the length of the longest common substring
    longest = 0

    # Split the strings into lists of characters
    list1 = list(s1)
    list2 = list(s2)

    # Iterate over each character of the strings
    for i in range(len(list1)):
        for j in range(len(list2)):
            # Compare the characters
            if list1[i] == list2[j]:
                # Increase the largest substring length by one
                longest += 1
            else:
                # Reset the longest substring length
                longest = 0

            # Update the shortest substring length
            shortest = min(len(list1) - i, len(list2) - j)

            # Return the longest common substring if it has reached the length of the shortest string
            if longest == shortest:
                return s1[i-longest+1:i+1]

# Return an empty string if the longest common substring length is 0
if longest == 0:
    return ""