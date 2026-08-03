states = ['A', 'B', 'C', 'D']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors = ['Red', 'Green', 'Blue']

assignment = {}

def is_safe(state, color):
    for neighbor in neighbors[state]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def solve(index):
    if index == len(states):
        return True

    state = states[index]

    for color in colors:
        if is_safe(state, color):
            assignment[state] = color

            if solve(index + 1):
                return True

            del assignment[state]

    return False

if solve(0):
    print("Map Coloring Solution:")
    for state in states:
        print(f"{state} -> {assignment[state]}")
else:
    print("No solution exists.")