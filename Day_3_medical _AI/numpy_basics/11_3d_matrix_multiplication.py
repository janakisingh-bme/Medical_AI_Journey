import numpy as np

A = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

B = np.array([
    [[1, 8],
     [0, 1]],

    [[2, 9],
     [0, 2]]
])

result = np.matmul(A, B)

print("Matrix multiplication:")
print(result)