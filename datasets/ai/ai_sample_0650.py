def simple_linear_regression(X, y): 
    # calculate the mean value of a list of numbers 
    def mean(values): 
        return sum(values) / float(len(values)) 

    # calculate covariance between x and y 
    def covariance(x, mean_x, y, mean_y): 
        covar = 0.0
        for i in range(len(x)): 
            covar += (x[i] - mean_x) * (y[i] - mean_y) 
        return covar 

    # calculate the variance of a list of numbers 
    def variance(values, mean): 
        return sum([(x - mean)**2 for x in values]) 
  
    # calculate coefficients 
    def coefficients(X, y): 
        x_mean, y_mean = mean(X), mean(y) 
        b1 = covariance(X, x_mean, y, y_mean) / variance(X, x_mean) 
        b0 = y_mean - b1 * x_mean 
        return [b0, b1] 
  
    b = coefficients(X, y) 
    return b[0], b[1]