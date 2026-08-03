from collections import deque

def is_valid(m_left, c_left):
    m_right = 3 - m_left
    c_right = 3 - c_left

    if (m_left > 0 and c_left > m_left):
        return False
    if (m_right > 0 and c_right > m_right):
        return False

    return True

def solve():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [])])
    visited = set()

    while queue:
        (m, c, boat), path = queue.popleft()

        if (m, c, boat) in visited:
            continue

        visited.add((m, c, boat))
        path = path + [(m, c, boat)]

        if (m, c, boat) == goal:
            return path

        moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

        for dm, dc in moves:
            if boat == 1:
                new_m = m - dm
                new_c = c - dc
                new_boat = 0
            else:
                new_m = m + dm
                new_c = c + dc
                new_boat = 1

            if (
                0 <= new_m <= 3 and
                0 <= new_c <= 3 and
                is_valid(new_m, new_c)
            ):
                queue.append(((new_m, new_c, new_boat), path))

    return None

solution = solve()

if solution:
    print("Missionaries Left | Cannibals Left | Boat")
    for state in solution:
        print(state)
else:
    print("No solution found.")