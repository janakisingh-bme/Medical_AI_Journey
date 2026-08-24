import matplotlib.pyplot as plt

subjects = ["Math", "Science", "Python", "English"]
marks = [80, 75, 90, 85]

plt.bar(subjects, marks)

plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Student Marks")

plt.show()