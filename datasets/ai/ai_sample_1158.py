import numpy as np
import random

# Define a fitness function
def fitness_function(x):
    return x ** 2 - 3 * x + 4
# Generate initial population
population = [random.uniform(-100,100) for _ in range(100)]
# Start a genetic algorithm to optimize the population
def genetic_algorithm(population):
    # Selection
    selected = np.random.choice(population, 50, replace=False)
    # Crossover
    offspring = []
    for i in range(0, len(selected)-1, 2):
        parent1, parent2 = selected[i], selected[i+1]
        cross_over_point = random.randint(0, len(parent1)-1)
        offspring_1 = np.concatenate([parent1[:cross_over_point], parent2[cross_over_point:]])
        offspring_2 = np.concatenate([parent2[:cross_over_point], parent1[cross_over_point:]])
        offspring.append(offspring_1)
        offspring.append(offspring_2)
    # Mutation
    for i in range(len(offspring)):
        for bit_index, bit_value in enumerate(offspring[i]):
            mutation_prob = random.random()
            if mutation_prob < 0.3:
                offspring[i][bit_index] = random.random() * 200 - 100
    # ELitism
    population = sorted(population, key=fitness_function, reverse=True)
    population = population[:10] + offspring
    # Return the new population
    return population

# Run the genetic algorithm
for i in range(500):
    population = genetic_algorithm(population)

# Find the optimal solution
opt_solution = max(population, key=fitness_function)
print("Optimum solution: {}".format(opt_solution))