import numpy as np
from sklearn.linear_model import LinearRegression

# Parameters for the genetic algorithm
num_generations = 50   # Number of generations
population_size = 20  # Population size

# Training data
X = np.array([[feature_1], [feature_2]]).T
y = np.array([[label]]).T

# Function to evaluate the fitness of a given individual
def get_fitness(individual):
 lin_ model = LinearRegression()
 model.fit(X, y)
 y_pred = model.predict(X)
 error = mean_squared_error(y_true, y_pred)
 return error

# Function to generate a single member of the population
def generate_individual():
 individual = [random.uniform(-1, 1) for x in range(2)]
 return individual

# Function to generate a whole population
def generate_population():
 population = [generate_individual() for x in range(population_size)]
 return population 

# Main loop of the genetic algorithm
population = generate_population()
for generation in range(num_generations):
 new_population = []
 for individual in population:
  # Evaluate the fitness of the individual
  fitness = get_fitness(individual)
  # Select the two best individuals based on their fitness
  mates = selection(population, fitness)
  # Crossover
  new_individual = crossover(mates)
  # Mutation
  new_individual = mutation(new_individual)
  # Add this individual to the new population
  new_population.append(new_individual)
 # Set the population to the new one
 population = new_population

# Print the optimal solution
optimal_solution = population[0] # Best individual is the first one
print("Optimal solution: ", optimal_solution)