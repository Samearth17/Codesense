import numpy as np

def fitness_function(X):
 return X[0] * X[1] + X[2]

def generate_genes(n, lower, upper):
 return np.random.uniform(lower, upper, n)

def GA(genes, fitness, lower, upper, mutation_rate, max_iterations):
 max_fitness = -float('inf')
 max_genes = None
 n = len(genes)
 for iteration in range(max_iterations):
 if max_fitness >= fitness_function(genes):
 break
 # Generate new population
 parent_generation = []
 for _ in range(int(n/2)):
 parent_generation.append((genes, fitness_function(genes)))
 parent_generation.sort(key=lambda x: x[1], reverse=True)  # Sort  parents 
 # Select the best
 elite_genes, elite_fitness = parent_generation[0]
 # Crossover
 child_generation = []
 for _ in range(int(n/2)):  # Breed new population
 parent_1 = np.random.choice(parent_generation)
 parent_2 = np.random.choice(parent_generation)
 child_1, child_2 = crossover(parent_1, parent_2, n)
 child_generation.append(child_1)
 child_generation.append(child_2)
 # Mutate
 mutants = []
 for child in child_generation:
 if np.random.uniform(0, 1) < mutation_rate:
 mutants.append(mutation(child, lower, upper))
 else:
 mutants.append(child)
 # Update 
 for gene in mutants:
 genes = gene
 fitness = fitness_function(genes)
 if fitness > max_fitness:
 max_fitness = fitness
 max_genes = gene
 return max_fitness, max_genes

def crossover(parent_1, parent_2, n):
 n_split = np.random.randint(1, n)  # Split 
 child_1 = np.concatenate([parent_1[:n_split], parent_2[n_split:]])
 child_2 = np.concatenate([parent_2[:n_split], parent_1[n_split:]])
 return child_1, child_2

def mutation(gene, lower, upper):
 for i, gene_value in enumerate(gene):
 if np.random.uniform(0, 1) < mutation_rate:
 gene[i] = np.random.uniform(lower, upper)
 return gene

# Run GA
n = 3
lower = 0
upper = 1
genes = generate_genes(n, lower, upper)
mutation_rate = 0.1
max_iterations = 1000
max_fitness, max_genes = GA(genes, fitness_function, lower, upper, mutation_rate, max_iterations)

# Print results
print("Maximum fitness score:", max_fitness)
print("Parameters:", max_genes)