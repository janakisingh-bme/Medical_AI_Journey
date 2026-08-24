import numpy as np

A = np.array([
    [
        [1, 2],
        [3, 4]
    ],
    [
        [5, 6],
        [7, 8]
    ]
])

print("Complete array:")
print(A)

print("second layer:")
print(A[1])

print("First row of second layer:")
print(A[1, 0])

print("First element of second row of second layer:")
print(A[1, 1, 0])