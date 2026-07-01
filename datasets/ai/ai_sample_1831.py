# Function to convert list to dictionary
def list_to_dict(my_list):
    """Converts a list to a dictionary."""
    my_dict = {}
    for item in my_list:
        my_dict[item[0]] = item[1]
    return my_dict

if __name__ == '__main__':
	# Sample list
    my_list = [("apple", "fruit"), ("carrot", "vegetable")]
    # Convert list to dictionary
    my_dict = list_to_dict(my_list)
    # Print dictionary
    print(my_dict)