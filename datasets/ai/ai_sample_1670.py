from math import factorial

def binomial_probability(n, p, x):
    """Find the probability of an event using the binomial distribution.

    Args:
        n (int): The number of trials.
        p (float): The probability of success of the event.
        x (int): The number of successes.

    Returns:
        float: The probability of x successes in n trials.
    """
    return factorial(n)/(factorial(x)*factorial(n-x)) * p**x * (1-p)**(n-x)

if __name__ == '__main__':
    n = 10
    p = 0.5
    x = 6
    result = binomial_probability(n, p, x)
    print(result)