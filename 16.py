import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

Y = np.array([[0], [0], [0], [1]])

weights = np.array([[1.0], [1.0]])
bias = -1.5

weighted_sum = np.dot(X, weights) + bias
output = sigmoid(weighted_sum)

print("Input\tPredicted Output\tTarget")

for i in range(len(X)):
    print(X[i], "\t", round(output[i][0], 3), "\t\t", Y[I][0])