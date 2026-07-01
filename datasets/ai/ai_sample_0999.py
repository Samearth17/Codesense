import random

# Define the equation
def calc_fitness(x): 
 return x**2 + x - 13

# Initialize the population
population = []

for _ in range(10):
 population.append(random.uniform(0, 10))

# Define the mutation function
def mutate(x):
 return x + random.uniform(-1, 1)

# Perform genetic algorithm
while True:
 # Calculate the fitness of each chromosome in the population
 population_fitness = [calc_fitness(x) for x in population]

 # Check if any chromosome matches the equation
 if 0 in population_fitness:
  break

 # Select the fittest chromosome
 fittest_idx = population_fitness.index(min(population_fitness))
 fittest = population[fittest_idx]

 # Create a new generation by mutating the fittest chromosome
 new_generation = [mutate(fittest) for _ in range(10)]

 # Replace the old population with the new one
 population = new_generation

# Print the fittest chromosome
print(f'Solution: {fittest}')