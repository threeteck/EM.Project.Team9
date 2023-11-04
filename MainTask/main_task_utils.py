import numpy as np
from tqdm import tqdm
from scipy.spatial.distance import pdist, squareform
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from glob import glob
from tqdm import tqdm

def sammons_error(X, Y):
    N = X.shape[0]
    sum_d = 0
    sum_error = 0

    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(X[i] - X[j])
            d_hat = np.linalg.norm(Y[i] - Y[j])

            if d != 0:
                err = ((d - d_hat) ** 2) / d
                sum_error += err
                sum_d += d

    return sum_error / sum_d if sum_d != 0 else 0

def get_distances(X):
    dist_X = squareform(pdist(X, 'euclidean'))
    return dist_X, np.sum(dist_X), np.sum(dist_X ** 2)

def optimized_sammons_error(dist_X, sum_d, sum_d_squared, Y): # sum_d_squared for compatibility
    dist_Y = squareform(pdist(Y, 'euclidean'))

    with np.errstate(divide='ignore', invalid='ignore'):
        delta = dist_X - dist_Y
        error = np.where(dist_X != 0, (delta ** 2) / dist_X, 0)

    return np.sum(error) / sum_d

def kruskals_stress(X, Y):
    N = X.shape[0]
    sum_d_squared = 0
    sum_stress = 0

    for i in range(N):
        for j in range(i + 1, N):
            d = np.linalg.norm(X[i] - X[j])
            d_hat = np.linalg.norm(Y[i] - Y[j])
            sum_d_squared += d ** 2
            sum_stress += (d - d_hat) ** 2

    return sum_stress / sum_d_squared if sum_d_squared != 0 else 0

def optimized_kruskals_stress(dist_X, sum_d, sum_d_squared, Y): # sum_d for compatibility
    dist_Y = squareform(pdist(Y, 'euclidean'))

    delta = dist_X - dist_Y
    sum_stress = np.sum(delta ** 2)

    return sum_stress / sum_d_squared if sum_d_squared != 0 else 0

def fitness_function(X, parameter_vector, cost_function, k):
    selected_metrics = X[:, parameter_vector.argsort()[-k:]]
    return cost_function(X, selected_metrics)

def get_fitness_function(X, cost_function, k):
    return lambda parameter_vector: fitness_function(X, parameter_vector, cost_function, k)

def optimized_fitness_function(X, X_dist, sum_d, sum_d_squared, parameter_vector, cost_function, k, cached_fitness_function):
    metrics = tuple(np.sort(parameter_vector.argsort()[-k:]))
    selected_metrics = X[:, metrics]
    if metrics not in cached_fitness_function:
        cached_fitness_function[metrics] = cost_function(X_dist, sum_d, sum_d_squared, selected_metrics)
    return cached_fitness_function[metrics]

def get_optimized_fitness_function(X, cost_function, k):
    dist_X, sum_d, sum_d_squared = get_distances(X)
    cached_fitness_function = {}
    return lambda parameter_vector: optimized_fitness_function(X, dist_X, sum_d, sum_d_squared, parameter_vector, cost_function, k, cached_fitness_function)

def pso(fitness_function, dim, num_particles=30, max_iter=100, bounds=None, w=0.5, c1=0.8, c2=0.9, verbose=False):
    """
    Particle Swarm Optimization (PSO) algorithm.

    Parameters:
    - fitness_function: The fitness function to be optimized.
    - dim: Dimensionality of the search space.
    - num_particles: Number of particles in the swarm.
    - max_iter: Maximum number of iterations.
    - bounds: Bounds for the search space as a tuple (min, max).
    - w: Inertia weight.
    - c1: Cognitive parameter.
    - c2: Social parameter.

    Returns:
    - The best solution found and its fitness.
    """
    # PSO parameters

    # Initialize the swarm
    if bounds:
        min_bound, max_bound = bounds
        particles = min_bound + (max_bound - min_bound) * np.random.rand(num_particles, dim)
    else:
        particles = np.random.rand(num_particles, dim)

    velocity = np.zeros((num_particles, dim))
    personal_best = particles.copy()
    personal_best_scores = np.array([fitness_function(p) for p in personal_best])
    global_best = personal_best[np.argmin(personal_best_scores)]
    global_best_score = min(personal_best_scores)

    # Iterate over max_iter
    for t in tqdm(range(max_iter), disable=not verbose):
        for i in range(num_particles):
            if verbose:
                print(f'Iteration {t + 1}/{max_iter}, particle {i + 1}/{num_particles} ', end='... ')
            # Update velocity
            r1, r2 = np.random.rand(2)
            velocity[i] = w * velocity[i] + c1 * r1 * (personal_best[i] - particles[i]) \
                          + c2 * r2 * (global_best - particles[i])

            # Update particle position
            particles[i] += velocity[i]
            if bounds:
                particles[i] = np.clip(particles[i], min_bound, max_bound)

            # Evaluate particle
            current_fitness = fitness_function(particles[i])

            # Update personal best
            if current_fitness < personal_best_scores[i]:
                personal_best[i] = particles[i].copy()
                personal_best_scores[i] = current_fitness

                # Update global best
                if current_fitness < global_best_score:
                    global_best = particles[i].copy()
                    global_best_score = current_fitness

            if verbose:
                print(f'Best fitness: {global_best_score}')

    return global_best, global_best_score

class GeneticAlgorithm:
    def __init__(self, fitness_function, population_size=100, num_features=10, num_generations=50, mutation_rate=0.01, crossover_rate=0.7, mutation_std=0.1, bounds=(0, 1)):
        self.fitness_function = fitness_function
        self.population_size = population_size
        self.num_features = num_features
        self.num_generations = num_generations
        self.mutation_rate = mutation_rate
        self.crossover_rate = crossover_rate
        self.mutation_std = mutation_std
        self.bounds = bounds
        self.population = np.random.rand(population_size, num_features) * (bounds[1] - bounds[0]) + bounds[0]

    def tournament_selection(self, fitness_scores, tournament_size=3):
        selected = np.random.choice(np.arange(self.population_size), size=tournament_size, replace=False)
        selected_fitness_scores = fitness_scores[selected]
        best_individual = np.argmin(selected_fitness_scores)
        return self.population[selected[best_individual]]

    def single_point_crossover(self, parent1, parent2):
        if np.random.rand() < self.crossover_rate:
            crossover_point = np.random.randint(1, self.num_features)
            child1 = np.concatenate([parent1[:crossover_point], parent2[crossover_point:]])
            child2 = np.concatenate([parent2[:crossover_point], parent1[crossover_point:]])
            return child1, child2
        else:
            return parent1, parent2

    def mutate(self, individual):
        for i in range(len(individual)):
            if np.random.rand() < self.mutation_rate:
                individual[i] += np.random.normal(0, self.mutation_std)
                individual[i] = np.clip(individual[i], self.bounds[0], self.bounds[1])
        return individual

    def evolve_population(self):
        new_population = []
        fitness = np.array([self.fitness_function(individual) for individual in self.population])

        for _ in range(self.population_size // 2):
            parent1 = self.tournament_selection(fitness)
            parent2 = self.tournament_selection(fitness)
            child1, child2 = self.single_point_crossover(parent1, parent2)
            new_population.append(self.mutate(child1))
            new_population.append(self.mutate(child2))

        self.population = np.array(new_population)

    def run(self, verbose=False):
        best_fitness = np.inf
        best_individual = None

        for generation in tqdm(range(self.num_generations), disable=not verbose):
            self.evolve_population()
            fitness = np.array([self.fitness_function(individual) for individual in self.population])
            best_idx = np.argmin(fitness)

            if fitness[best_idx] < best_fitness:
                best_fitness = fitness[best_idx]
                best_individual = self.population[best_idx]

        return best_individual, best_fitness

def compute_scores(project_name, k, X):
    sammon_error_fitness_function = get_optimized_fitness_function(X, optimized_sammons_error, k)
    kruskal_stress_fitness_function = get_optimized_fitness_function(X, optimized_kruskals_stress, k)

    # Particle Swarm Optimization
    best_solution_pso_sammon, best_fitness_pso_sammon = pso(sammon_error_fitness_function, dim=X.shape[1], num_particles=30, max_iter=30, bounds=(0, 1))
    best_solution_pso_kruskal, best_fitness_pso_kruskal = pso(kruskal_stress_fitness_function, dim=X.shape[1], num_particles=30, max_iter=30, bounds=(0, 1))

    # Genetic Algorithm
    ga_sammon = GeneticAlgorithm(sammon_error_fitness_function, population_size=30, num_features=X.shape[1], num_generations=30, mutation_rate=0.1, crossover_rate=0.7, mutation_std=0.25, bounds=(0, 1))
    best_solution_ga_sammon, best_fitness_ga_sammon = ga_sammon.run()

    ga_kruskal = GeneticAlgorithm(kruskal_stress_fitness_function, population_size=30, num_features=X.shape[1], num_generations=30, mutation_rate=0.1, crossover_rate=0.7, mutation_std=0.25, bounds=(0, 1))
    best_solution_ga_kruskal, best_fitness_ga_kruskal = ga_kruskal.run()

    return (k, best_solution_pso_sammon, best_solution_pso_kruskal, best_fitness_pso_sammon, best_fitness_pso_kruskal, best_solution_ga_sammon, best_solution_ga_kruskal, best_fitness_ga_sammon, best_fitness_ga_kruskal)