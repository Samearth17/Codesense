# define the function
def calculate_probability(probability_data, event):
 # define the probability of the event
 probability = 0

 # iterate over each probability in the data
 for p in probability_data:
 # check if the event matches
 if event == p:
 # add the probability to the sum
 probability += p

 # return the calculated probability
 return probability

# the input
probability_data = [0.4, 0.6, 0.2, 0.9]
event = "A"

# call the function
probability = calculate_probability(probability_data, event)

# print the result
print(f"The probability of event {event} happening is {probability}")