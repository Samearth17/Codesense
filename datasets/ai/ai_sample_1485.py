import pandas as pd
import numpy as np

def fill_missing_values(df, colname):

    # get a list of all the users in the dataframe
    users = df['username'].values.tolist()
    
    for i, user in enumerate(users):
        if df[colname].isnull()[i] == True:
            closest_neighbors = find_closest_neighbors(df, user, 3)
            df[colname][i] = np.mean([df[colname][j] for j in closest_neighbors])
    
    return df

def find_closest_neighbors(df, user, k):
    closest_neighbors = []
    user_age = df[df.username == user].age.values[0]
    for v in df.index:
        if df.username[v] != user and len(closest_neighbors) < k:
            # compute the Euclidean distance
            dist = np.sqrt(np.abs(user_age - df.age[v])**2)
            closest_neighbors.append((v, dist))
    
    closest_neighbors.sort(key=lambda x: x[1])
    return [neighbor[0] for neighbor in closest_neighbors]