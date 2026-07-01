def findAnomaly(data):
  mean = []
  std = []
  for column in data.T:
    mean.append(np.mean(column))
    std.append(np.std(column))
  
  anomalies = []
  for row in data:
    zscore = []
    for i in range(len(mean)):
      zscore.append((row[i] - mean[i])/std[i])
    if np.max(zscore) > 2:
      anomalies.append(row)

  return anomalies