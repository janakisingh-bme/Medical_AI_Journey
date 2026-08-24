import matplotlib.pyplot as plt

marks = [45, 50, 55, 60, 65, 70, 72, 75, 80, 85, 90, 95]

plt.hist(marks, bins=5)

plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")

plt.show()
