import random
import numpy as np

# Define the cost function
def cost(x):
 return x**2
 
# Initialize the population
population_size = 20
population = [random.randint(0, 100) for _ in range(population_size)]

# Perform the optimization
max_generation = 100
for _ in range(max_generation):
 # Calculate the fitness
 fitness = [cost(x) for x in population]
 
 # Select the fittest individuals
 fittest_individuals = np.argsort(fitness)[::-1][:int(population_size/2)]
 
 # Generate the new population
 new_population = []
 for individual in fittest_individuals:
  new_population.append(population[individual])
  new_population.append(population[individual] + random.randint(-5, 5))
 population = new_population
 
# Print the result
print(population)