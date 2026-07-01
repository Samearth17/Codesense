import numpy as np
def geneticAlgorithm(population, iter):
    for i in range(iter):
        new_population = []
        
        for chromosome in population:
            cost = getCost(chromosome)
            fitness = 1/cost
            parent1, parent2 = selectParents(population)
            offspring = crossover(parent1, parent2)
            offspring = mutation(offspring)
            new_population.append(offspring)
            
        population = new_population
    return population
    
def selectParents(population):
    parent1, parent2 = getRandomParents(population)
    fitness1 = getCost(parent1)
    fitness2 = getCost(parent2)
    if (fitness1 < fitness2):
        return parent1, parent2
    else:
        return parent2, parent1
        
def getRandomParents(population):
    parent1 = population[np.random.randint(0, len(population))]
    parent2 = population[np.random.randint(0, len(population))]
    while (parent1 == parent2):
        parent2 = population[np.random.randint(0, len(population))]
    return parent1, parent2
    
def crossover(parent1, parent2):
    '''
    Insert code to perform crossover here
    '''
    return offspring
    
def mutation(offspring):
    '''
    Insert code to perform mutation here
    '''
    return offspring
    
def getCost(chromosome):
    '''
    Insert code to compute the cost for a chromosome here
    '''
    return cost