import numpy as np

def detect_outliers(data):
    # calculate summary statistics
    data_mean, data_std = np.mean(data), np.std(data)
    
    # define outliers
    cut_off = data_std * 3
    lower, upper = data_mean - cut_off, data_mean + cut_off
    
    # identify outliers
    outliers = [x for x in data if x < lower or x > upper]
    return outliers

dataset = [6, 7, 8, 10, 8, 8, 9, 11, 12, 15]
outliers = detect_outliers(dataset) 
print(outliers)  # [15]