#Calculate total amount of time spent by a user on a website

def total_time_spent(time_spent):
    """
    Calculates the total amount of time spent by a user on a website
    
    Parameters
    ----------
    time_spent : list
        List of times, in seconds, spent by the user on the website
        
    Returns
    -------
    total : float
        Total amount of time, in minutes, spent by the user
    """
    # Initialise total to 0 
    total = 0
    
    # Loop through the list and calculate total 
    for t in time_spent:
        total += t
    
    # Tranform the time from seconds to minutes
    total_minutes = total/60
    
    return total_minutes

#Test
time_spent = [120, 60, 90, 5, 10, 45]
total = total_time_spent(time_spent)
print("Total time spent (minutes):", total)