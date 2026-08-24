import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("Original array:")
print(A)

B = np.transpose(A)

print("Transpose:")
print(B)