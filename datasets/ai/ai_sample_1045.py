import csv 
import numpy as np 
  
def read_csv(filename): 
    data = [] 
    with open(filename, 'r') as csvfile: 
        csvreader = csv.reader(csvfile) 
        for row in csvreader: 
            data.append(row) 
    return np.array(data).astype(float) 
  
def compute_corrcoef(data): 
    corrcoefs = [] 
    for i in range(data.shape[1]): 
        for j in range(i + 1, data.shape[1]): 
            r = np.corrcoef(data[:,i], data[:, j])[0,1] 
            corrcoefs.append((i, j, r)) 
    return np.array(corrcoefs)