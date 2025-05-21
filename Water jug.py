def water_jug_bfs(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = []

    # Initial state: both jugs are empty
    queue.append((0, 0))

    while queue:
        (jug1, jug2) = queue.pop(0)

        # If we've already seen this state, skip
        if (jug1, jug2) in visited:
            continue

        visited.add((jug1, jug2))
        print(f"Jug1: {jug1} | Jug2: {jug2}")

        # Check if we reached the target
        if jug1 == target or jug2 == target:
            print("Target achieved!")
            return

        # All possible next states
        next_states = [
            (jug1_capacity, jug2),              # Fill Jug1
            (jug1, jug2_capacity),              # Fill Jug2
            (0, jug2),                          # Empty Jug1
            (jug1, 0),                          # Empty Jug2
            (0, jug1 + jug2) if jug1 + jug2 <= jug2_capacity else (jug1 - (jug2_capacity - jug2), jug2_capacity),  # Jug1 -> Jug2
            (jug1 + jug2, 0) if jug1 + jug2 <= jug1_capacity else (jug1_capacity, jug2 - (jug1_capacity - jug1))   # Jug2 -> Jug1
        ]

        for state in next_states:
            if state not in visited:
                queue.append(state)

# Example: 4L and 3L jugs, target = 2L
water_jug_bfs(4, 3, 2)
