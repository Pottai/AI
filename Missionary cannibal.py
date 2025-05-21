def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    # Check missionaries not outnumbered
    if (M_left > 0 and M_left < C_left) or (M_right > 0 and M_right < C_right):
        return False
    return 0 <= M_left <= 3 and 0 <= C_left <= 3

def get_successors(state):
    M, C, boat = state
    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]
    successors = []

    for m, c in moves:
        if boat == 'left':
            new_state = (M - m, C - c, 'right')
        else:
            new_state = (M + m, C + c, 'left')

        if is_valid(new_state):
            successors.append(new_state)

    return successors

def bfs():
    start = (3, 3, 'left')
    goal = (0, 0, 'right')
    queue = [(start, [start])]
    visited = []

    while queue:
        current_state, path = queue.pop(0)

        if current_state in visited:
            continue
        visited.append(current_state)

        if current_state == goal:
            return path

        for next_state in get_successors(current_state):
            if next_state not in visited:
                queue.append((next_state, path + [next_state]))

    return None

# Run the BFS
solution = bfs()
if solution:
    print("Solution steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
