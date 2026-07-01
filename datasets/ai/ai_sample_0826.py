# Function to calculate mean of two classes
def calculate_means(dataset):
    class_0_total = 0
    class_1_total = 0
    for data_point in dataset:
        if data_point[2] == 0:
            class_0_total += 1
        else:
            class_1_total += 1
    class_0_mean = class_0_total / len(dataset)
    class_1_mean = class_1_total / len(dataset)
    return [class_0_mean, class_1_mean]

# Function to classify a new point
def classify(data_point, means):
    if data_point[2] <= means[0]:
        print("Class 0")
    else:
        print("Class 1")

# Main 
data = [['men', 'sports', 1], ['women', 'foods', 0], ['men', 'foods', 1], ['women', 'sports', 0]]
means = calculate_means(data)
new_data = ['men', 'sports', 0.5]
classify(new_data, means)