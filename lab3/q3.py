# 3. Genetic Algorithms: 10*5=50
# Problem Statement:
# You are tasked with solving the Traveling Salesman Problem (TSP) using a genetic algorithm.
# Given a set of cities and their pairwise distances, your goal is to find the shortest possible route
# that visits each city exactly once and returns to the original city.
# Requirements:
# 1. Implement a genetic algorithm from scratch using a programming language of your choice.
# 2. Use a suitable representation (e.g., permutation encoding) to represent candidate solutions.
# 3. Define appropriate genetic operators (e.g., selection, crossover, mutation) for the TSP.
# 4. Implement the fitness function to evaluate the quality of each candidate solution.
# 5. Run the genetic algorithm for a specified number of generations and return the best solution
# found.
# Generate city maps of a few dozen cities and log the improvements over the generations

import numpy as np


class TSP:

    def __init__(self, cities, distances):
        self.cities = cities
        self.distances = distances
        self.best_fitness = np.inf
        self.best_route = None

    def get_distance(self, city1, city2):
        return self.distances[city1][city2]

    def get_fitness(self, route):
        fitness = 0
        for i in range(len(route)):
            fitness += self.get_distance(route[i], route[(i+1) % len(route)])
        return fitness

    def get_random_route(self):
        return np.random.permutation(self.cities)

    def crossover(self, route1, route2):
        child = np.zeros(len(route1), dtype=int)
        for i in range(len(route1)):
            if route1[i] in route2:
                child[i] = route1[i]
        for i in range(len(route1)):
            if child[i] == 0:
                for j in range(len(route1)):
                    if route2[j] not in child:
                        child[i] = route2[j]
                        break
        return child

    def mutate(self, route):
        i = np.random.randint(len(route))
        j = np.random.randint(len(route))
        route[i], route[j] = route[j], route[i]
        return route

    def run(self, generations, population_size, crossover_rate, mutation_rate):
        population = []
        for i in range(population_size):
            population.append(self.get_random_route())
        for generation in range(generations):
            fitnesses = []
            for route in population:
                fitness = self.get_fitness(route)
                fitnesses.append(fitness)
                if fitness < self.best_fitness:
                    self.best_fitness = fitness
                    self.best_route = route
            fitnesses = np.array(fitnesses)
            fitnesses = fitnesses/fitnesses.sum()
            new_population = []
            for i in range(population_size):
                route1 = population[np.random.choice(
                    population_size, p=fitnesses)]
                route2 = population[np.random.choice(
                    population_size, p=fitnesses)]
                child = self.crossover(route1, route2)
                if np.random.rand() < mutation_rate:
                    child = self.mutate(child)
                new_population.append(child)
            population = new_population
        return self.best_route, self.best_fitness

    def print_route(self, route):
        for city in route:
            print(self.cities[city], end=' ')
        print(self.cities[route[0]])


tsp = TSP([0, 1, 2, 3, 4], [[0, 10, 15, 20, 25],
                            [10, 0, 35, 25, 20], 
                            [15, 35, 0, 30, 10], 
                            [20, 25, 30, 0, 15], 
                            [25, 20, 10, 15, 0]])

route, fitness = tsp.run(100, 100, 0.8, 0.1)
print('Best route: ', route)
print('Best fitness: ', fitness)

tsp.print_route(route)
