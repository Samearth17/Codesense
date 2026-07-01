def predict_category(data, sample):
    if not data:
        return None

    # Count the number of samples in each category
    categories = {}
    for d in data:
        if d['category'] in categories:
            categories[d['category']] += 1
        else:
            categories[d['category']] = 1

    # Find the majority category
    majority_cat = None
    majority_cat_count = 0
    for cat, count in categories.items():
        if count > majority_cat_count:
            majority_cat = cat
            majority_cat_count = count
    
    # Predict the sample category as the majority category
    return majority_cat