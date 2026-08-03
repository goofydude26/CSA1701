import math

def alpha_beta(depth, node_index, is_max, values, alpha, beta, max_depth):
    if depth == max_depth:
        return values[node_index]

    if is_max:
        best = -math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                False,
                values,
                alpha,
                beta,
                max_depth
            )

            best = max(best, value)
            alpha = max(alpha, best)

            if beta <= alpha:
                break

        return best

    else:
        best = math.inf

        for i in range(2):
            value = alpha_beta(
                depth + 1,
                node_index * 2 + i,
                True,
                values,
                alpha,
                beta,
                max_depth
            )

            best = min(best, value)
            beta = min(beta, best)

            if beta <= alpha:
                break

        return best

values = [3, 5, 6, 9, 1, 2, 0, -1]

max_depth = int(math.log2(len(values)))

result = alpha_beta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    max_depth
)

print("Optimal Value:", result)