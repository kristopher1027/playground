import matplotlib.pyplot as plt

student = {
    "name": "Christopher",
    "scores": {
        "Math": 80,
        "Python": 95,
        "Database": 75,
        "AI": 90
    }
}


subjects = list(student["scores"].keys())

marks = list(student["scores"].values())


plt.bar(subjects, marks)

plt.title(f"{student['name']} Scores")

plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.savefig("student_scores.png")