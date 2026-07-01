def gini(x):
    """Calculate Gini Coefficient of a given dataset."""
    # calculate the frequency of each item in x
    x_value_counts = x.value_counts().sort_index() 

    # calculate the cumulative sum of x_value_counts
    x_cum_sum = x_value_counts.cumsum()

    # calculate the Lorenz values
    n = len(x)
    lorenz = x_cum_sum / n
    lorenz = np.insert(lorenz, 0, 0) # add 0 to the beginning of array

    # calculate the Gini Coefficient
    width = lorenz[:-1] - lorenz[1:]
    gini_coef = (1 / n) * sum(width * (lorenz[1:] + lorenz[:-1]))

    return gini_coef

if __name__ == '__main__':
    x = np.array([2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,21])
    gini_coef = gini(x)
    print(gini_coef) # should print 0.605