def most_frequent_element(list):
	# Create a dictionary to store the count of each element
	element_counts = {}

	# Iterate over the elements of the list
	for element in list:
		# Update the count in the dictionary
		if element in element_counts:
			element_counts[element] += 1
		else:
			element_counts[element] = 1

	# Find the most frequent element by comparing counts
	most_frequent_element = None
	most_frequent_count = 0
	for element, count in element_counts.items():
		if count > most_frequent_count:
			most_frequent_element = element
			most_frequent_count = count

	# Return the most frequent element
	return most_frequent_element