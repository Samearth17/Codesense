# Python Program to Implement 
# Traveling Salesman Problem using Genetic Algorithm 
import numpy as np 
from GeneticAlgorithm import GeneticAlgorithm 
class TSP(GeneticAlgorithm): 
	def __init__(self, distances): 
		super().__init__(distances) 
		self.distances = distances 
		self.n_cities = len(self.distances) 
		self.init_population(pop_size= 150, chromosome_length=self.n_cities) 

	def init_population(self, pop_size, chromosome_length):	 
		self.population = np.zeros((pop_size, chromosome_length)).astype(np.uint8) 
		for i, chromosome in enumerate(self.population): 
			np.random.shuffle(chromosome)
                      
	def fitness(self, chromosome): 
		current = 0
		fitness = 0
		for gene in chromosome: 
			fitness += self.distances[current][gene] 
			current = gene 
                    
		return fitness 
              
	def selection(self): 
		return np.argsort(self.fitness_value)[::-1][:int(self.pop_size/2)] 
          
	def crossover(self, parent_1, parent_2): 
		index = np.random.randint(1, self.chromosome_len - 1) 
        
		child_1 = np.hstack((parent_1[0:index], parent_2[index:])) 
		child_2 = np.hstack((parent_2[0:index], parent_1[index:])) 
        
		return child_1, child_2
          
	def mutation(self, chromosome): 
		index_1 = np.random.randint(0, self.chromosome_len) 
		index_2 = np.random.randint(0, self.chromosome_len) 
        
		temp = chromosome[index_1] 
		chromosome[index_2] = temp 
		return chromosome
          
if __name__ == '__main__': 
	distances = [[0, 755, 463, 493], 
	             [755, 0, 689, 582], 
	             [463, 689, 0, 744], 
	             [493, 582, 744, 0]] 

	tsp = TSP(distances) 
	tsp.run() 
	tsp.show_result()