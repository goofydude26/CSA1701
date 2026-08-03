from collections import deque

def water_jug(cap1, cap2, target):
    visited = set()
    queue = deque([((0, 0), [])])

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) in visited:
            continue

        visited.add((x, y))
        path = path + [(x, y)]

        if x == target or y == target:
            return path

        next_states = [
            (cap1, y),                    # Fill Jug 1
            (x, cap2),                    # Fill Jug 2
            (0, y),                       # Empty Jug 1
            (x, 0),                       # Empty Jug 2
            (max(0, x - (cap2 - y)), min(cap2, x + y)),  # Pour Jug 1 -> Jug 2
            (min(cap1, x + y), max(0, y - (cap1 - x)))   # Pour Jug 2 -> Jug 1
        ]

        for state in next_states:
            if state not in visited:
                queue.append((state, path))

    return None

jug1 = 4
jug2 = 3
target = 2

solution = water_jug(jug1, jug2, target)

if solution:
    print("Steps:")
    for step in solution:
        print(step)
else:
    print("No solution exists.")