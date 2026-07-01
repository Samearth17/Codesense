import numpy as np 
import matplotlib.pyplot as plt

def detect_anomalies(data):
    '''This function detects anomalies in a time series.'''
    # calculate rolling mean and rolling standard deviation
    rolling_mean = np.mean(data, axis=0)
    rolling_std = np.std(data, axis=0)

    # create an empty dataframe
    anomalies_df = []

    # detect anomalies
    for i in range(len(data)): 
        z_score = (data[i] - rolling_mean) / rolling_std
        if np.abs(z_score) > 3:
            anomalies_df.append(data[i])

    # plot the anomalies
    plt.plot(data, color='blue', label='Original data')
    plt.scatter(range(len(data)), anomalies_df, color='red', label='Anomalies')
    plt.legend()
    plt.show()