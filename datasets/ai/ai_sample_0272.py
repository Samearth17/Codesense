def validate_billing_address(address):
    # Split address into individual elements
    street, city_state_zip = address.split("\n")

    # Check street element
    if not street:
        return False
    
    # Check city_state_zip element
    elements = city_state_zip.split(",")
    if len(elements) != 2:
        return False
    city, state_zip = elements
    state, zip = state_zip.split(" ")
    if len(zip) != 5 or not zip.isdigit():
        return False
    
    return True