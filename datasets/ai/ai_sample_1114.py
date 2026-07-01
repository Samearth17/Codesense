def categorize(word):
    categories = {
        "fruits": ["apple", "orange", "banana"],
        "vegetables": ["carrot", "potato", "pepper"],
        "animals": ["dog", "cat", "bird"]
    }

    for category, words in categories.items():
        if word in words:
            return category

    return "unknown"


word = "apple"
category = categorize(word)
print(category)