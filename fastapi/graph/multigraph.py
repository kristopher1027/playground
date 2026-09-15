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


# Bar chart
plt.figure()
plt.bar(subjects, marks)
plt.title("Christopher's Scores")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.savefig("bar_chart.png")
plt.close()


# Pie chart
plt.figure()
plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Christopher's Scores")
plt.savefig("pie_chart.png")
plt.close()


# Line graph
plt.figure()
plt.plot(subjects, marks, marker="o")
plt.title("Christopher's Scores")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.savefig("line_graph.png")
plt.close()


# Scatter graph
plt.figure()
plt.scatter(subjects, marks)
plt.title("Christopher's Scores")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.savefig("scatter_graph.png")
plt.close()


# Horizontal bar graph
plt.figure()
plt.barh(subjects, marks)
plt.title("Christopher's Scores")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.savefig("horizontal_bar.png")
plt.close()



## venv/bin/python graph/multigraph.py