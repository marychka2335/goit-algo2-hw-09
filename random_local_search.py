import random

# Random Local Search
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    dim = len(bounds)
    best_solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
    best_value = func(best_solution)

    for _ in range(iterations):
        candidate_solution = [random.uniform(bounds[i][0], bounds[i][1]) for i in range(dim)]
        candidate_value = func(candidate_solution)

        if candidate_value < best_value:
            best_solution, best_value = candidate_solution, candidate_value

        if abs(candidate_value - best_value) < epsilon:
            break

    return best_solution, best_value
