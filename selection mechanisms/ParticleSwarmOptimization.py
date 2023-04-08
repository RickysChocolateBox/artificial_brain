import numpy as np

class ParticleSwarmOptimization:
    def __init__(self, fitness_function, num_particles, num_dimensions, w, c1, c2, max_iterations):
        self.fitness_function = fitness_function
        self.num_particles = num_particles
        self.num_dimensions = num_dimensions
        self.w = w
        self.c1 = c1
        self.c2 = c2
        self.max_iterations = max_iterations
        self.global_best_position = None
        self.global_best_fitness = float('inf')
        self.particles = self.initialize_particles()

    def initialize_particles(self):
        particles = []
        for i in range(self.num_particles):
            position = np.random.uniform(-1, 1, size=self.num_dimensions)
            velocity = np.zeros(self.num_dimensions)
            particle = Particle(position, velocity)
            particles.append(particle)
        return particles

    def optimize(self):
        for i in range(self.max_iterations):
            for particle in self.particles:
                particle.evaluate_fitness(self.fitness_function)
                if particle.fitness < self.global_best_fitness:
                    self.global_best_fitness = particle.fitness
                    self.global_best_position = particle.position
            for particle in self.particles:
                particle.update_velocity(self.w, self.c1, self.c2, self.global_best_position)
                particle.update_position()
    
class Particle:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity
        self.fitness = None
        self.best_position = position
        self.best_fitness = float('inf')

    def evaluate_fitness(self, fitness_function):
        self.fitness = fitness_function(self.position)
        if self.fitness < self.best_fitness:
            self.best_fitness = self.fitness
            self.best_position = self.position

    def update_velocity(self, w, c1, c2, global_best_position):
        r1 = np.random.uniform(size=self.position.shape)
        r2 = np.random.uniform(size=self.position.shape)
        cognitive_component = c1 * r1 * (self.best_position - self.position)
        social_component = c2 * r2 * (global_best_position - self.position)
        self.velocity = w * self.velocity + cognitive_component + social_component

    def update_position(self):
        self.position = self.position + self.velocity

