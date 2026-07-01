def define_category(num, criteria):
    if num >= criteria["low"][0] and num <= criteria["low"][1]:
        return "low"
    elif num >= criteria["medium"][0] and num <= criteria["medium"][1]:
        return "medium"
    elif num >= criteria["high"][0] and num <= criteria["high"][1]:
        return "high"
    else:
        return "not found"

num = 28 
criteria = {
    "low": [0,15],
    "medium": [16,30],
    "high": [31,99]
}

category = define_category(num, criteria)

print(category)