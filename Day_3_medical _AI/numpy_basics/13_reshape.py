import numpy as np

A = np.array([1, 2, 3, 4, 5, 6])

print("Original array:")
print(A)

B = A.reshape(3, 2)


print("Reshaped array:")
print(B)
print(B.ndim)
print(B.shape)