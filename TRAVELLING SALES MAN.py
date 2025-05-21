from itertools import permutations

# Define the distance matrix
# Example: 4 cities with distances between them
distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

def tsp_brute_force(distances):
    n = len(distances)
    cities = list(range(n))
    min_cost = float('inf')
    best_path = []

    for perm in permutations(cities[1:]):  # Fix the first city (0)
        path = [0] + list(perm) + [0]
        cost = 0
        for i in range(len(path) - 1):
            cost += distances[path[i]][path[i + 1]]
        if cost < min_cost:
            min_cost = cost
            best_path = path

    return best_path, min_cost

# Run the algorithm
path, cost = tsp_brute_force(distances)
print("Best path:", path)
print("Minimum cost:", cost)
