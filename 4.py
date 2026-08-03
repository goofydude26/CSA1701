from itertools import permutations

letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')

for perm in permutations(range(10), len(letters)):
    values = dict(zip(letters, perm))

    if values['S'] == 0 or values['M'] == 0:
        continue

    send = (
        values['S'] * 1000 +
        values['E'] * 100 +
        values['N'] * 10 +
        values['D']
    )

    more = (
        values['M'] * 1000 +
        values['O'] * 100 +
        values['R'] * 10 +
        values['E']
    )

    money = (
        values['M'] * 10000 +
        values['O'] * 1000 +
        values['N'] * 100 +
        values['E'] * 10 +
        values['Y']
    )

    if send + more == money:
        print("Solution Found:")
        print(values)
        print(f"\nSEND  = {send}")
        print(f"MORE  = {more}")
        print(f"MONEY = {money}")
        break