def probability_of_two_events(probability_of_first_event, probability_of_second_event):
    """
    Calculates the probability of two independent events occurring simultaneously.
    
    Args:
        probability_of_first_event (float): The probability of the first event occuring.
        probability_of_second_event (float): The probability of the second event occuring.
    
    Returns: 
        float: The probability of both events occurring simultaneously.
    """
       
    probability = probability_of_first_event * probability_of_second_event
    
    return probability