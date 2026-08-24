import numpy as np

A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print("Original array:")
print(A)

print("Selected part:")
print(A[1:3, 1:3])