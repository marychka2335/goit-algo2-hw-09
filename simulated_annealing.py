import random
import math

# Simulated Annealing
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    dim = len(bounds)
    current_solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    current_value = func(current_solution)
    best_solution, best_value = current_solution, current_value

    for _ in range(iterations):
        next_solution = [current_solution[i] + random.uniform(-epsilon, epsilon) for i in range(dim)]
        next_solution = [max(min(next_solution[i], bounds[i][1]), bounds[i][0]) for i in range(dim)]
        next_value = func(next_solution)

        if next_value < current_value or random.uniform(0, 1) < math.exp(-(next_value - current_value) / temp):
            current_solution, current_value = next_solution, next_value

        if next_value < best_value:
            best_solution, best_value = next_solution, next_value

        temp *= cooling_rate

        if temp < epsilon:
            break

    return best_solution, best_value
