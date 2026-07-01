import random

def cost(x):
    # compute the cost of x

def generate_population(size):
    # generate a population of size 'size'

def mutation(x):
    # randomize a single gene of x

def selection(population):
    # select two elements from the population for crossover

def crossover(x1, x2):
    # produce two offsprings using crossover

# initialize population
population = generate_population(50)

# repeat until convergence (or until a maximum number of iterations is reached)
while True:
    # select two parents
    x1, x2 = selection(population)
      
    # produce two offsprings by crossover
    offspring1, offspring2 = crossover(x1, x2)
          
    # mutation
    offspring1 = mutation(offspring1)
    offspring2 = mutation(offspring2) 
          
    # add offsprings to population
    population.append(offspring1)
    population.append(offspring2)

# select best solution
best_x = min(population, key=cost)