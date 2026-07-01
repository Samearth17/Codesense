def optimize_memory_usage(data):
    """Optimize memory usage when processing large datasets."""
    # Store ID and X, Y, Z in separate arrays
    ID = []
    X = []
    Y = []
    Z = []
    for row in data:
        ID.append(row[0])
        X.append(row[1])
        Y.append(row[2])
        Z.append(row[3])

    # Reduce data types to the most appropriate format
    ID = [int(x) for x in ID]
    X = [float(x) for x in X]
    Y = [float(x) for x in Y]
    Z = [float(x) for x in Z]

    # Return reshaped arrays as a single object
    return (ID, X, Y, Z)