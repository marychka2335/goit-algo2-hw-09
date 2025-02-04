import random

# Hill Climbing
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    current_solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    current_value = func(current_solution)

    for _ in range(iterations):
        next_solution = [current_solution[i] + random.uniform(-epsilon, epsilon) for i in range(dim)]
        next_solution = [max(min(next_solution[i], bounds[i][1]), bounds[i][0]) for i in range(dim)]
        next_value = func(next_solution)

        if next_value < current_value:
            current_solution, current_value = next_solution, next_value

        if abs(next_value - current_value) < epsilon:
            break

    return current_solution, current_value
