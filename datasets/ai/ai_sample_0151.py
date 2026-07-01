def find_matches(query, choices, threshold):
    # Convert query and choices to lower case
    query, choices = query.lower(), [choice.lower() for choice in choices]
    # Initialize empty list to store matches
    matches = []
    
    # Loop through each choice
    for choice in choices:
        # Calculate Levenshtein distance between query and choice
        distance = levenshtein_distance(query, choice)
        # If distance is less than threshold, append choice to matches
        if distance <= threshold:
            matches.append(choice)
    
    return matches