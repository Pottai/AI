from collections import deque

def is_valid(state):
    m_left, c_left, b_left, m_right, c_right, b_right = state

    if m_left < 0 or c_left < 0 or m_right < 0 or c_right < 0:
        return False
    if m_left > 0 and m_left < c_left:
        return False
    if m_right > 0 and m_right < c_right:
        return False
    return True

def successors(state):
    m_left, c_left, b_left, m_right, c_right, b_right = state
    moves = []

    if b_left == 1:
        for delta_m, delta_c in [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]:
            new_state = (
                m_left - delta_m, c_left - delta_c, 0,
                m_right + delta_m, c_right + delta_c, 1
            )
            if is_valid(new_state):
                moves.append(new_state)
    else:
        for delta_m, delta_c in [(0, 1), (0, 2), (1, 0), (1, 1), (2, 0)]:
            new_state = (
                m_left + delta_m, c_left + delta_c, 1,
                m_right - delta_m, c_right - delta_c, 0
            )
            if is_valid(new_state):
                moves.append(new_state)

    return moves

def bfs(initial_state):
    goal_state = (0, 0, 0, 3, 3, 1)
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal_state:
            return path + [state]

        visited.add(state)

        for successor_state in successors(state):
            if successor_state not in visited:
                queue.append((successor_state, path + [state]))

    return None

def print_solution(solution):
    if solution:
        for i, state in enumerate(solution):
            m_left, c_left, b_left, m_right, c_right, b_right = state
            print(f"Step {i}: Left bank - {m_left} missionaries, {c_left} cannibals | Right bank - {m_right} missionaries, {c_right} cannibals")
    else:
        print("No solution found.")

# Input section
m_left = int(input("Enter the number of missionaries on the left bank: "))
c_left = int(input("Enter the number of cannibals on the left bank: "))
b_left = 1

m_right = 3 - m_left
c_right = 3 - c_left
b_right = 0

initial_state = (m_left, c_left, b_left, m_right, c_right, b_right)
solution = bfs(initial_state)
print_solution(solution)
