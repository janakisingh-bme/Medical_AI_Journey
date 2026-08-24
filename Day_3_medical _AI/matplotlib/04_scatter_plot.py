import matplotlib.pyplot as plt

age = [20, 25, 30, 35, 40]
heart_rate = [75, 80, 85, 90, 95]

plt.scatter(age, heart_rate)

plt.xlabel("Age")
plt.ylabel("Heart Rate")
plt.title("Age vs Heart Rate")

plt.show()