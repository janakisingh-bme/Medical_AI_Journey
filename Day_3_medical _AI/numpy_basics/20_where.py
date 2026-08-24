import numpy as np

heart_rate = np.array([65, 72, 110, 75, 120, 80])

result = np.where(heart_rate > 100)

print("Heart rate:", heart_rate)
print("Positions above 100:", result)