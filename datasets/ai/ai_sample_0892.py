def optimize_function(x):
    return 3*x**2 + 8*x + 7

def objective_function(x):
    return optimize_function(x)

def optimize():
    optimal_x = 0
    min_val = objective_function(optimal_x)

    for x in range(1, 1000):
        current_val = objective_function(x)
        if current_val < min_val:
            min_val = current_val
            optimal_x = x

    return optimal_x