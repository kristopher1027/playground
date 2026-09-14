import statistics

student = {
    "name": "christopher",
    "scores": [80,80, 70, 100, 50, 90, 70]
}
minimum = sum(student["scores"])
average = statistics.mean(student["scores"])
maximum = max(student["scores"])
minimum = min(student["scores"])


print(student["name"])
print("maximum: ", maximum)
print("minimum: ", minimum)
print("Average:",f"{average:.2f}")


"=========================================="

import statistics


def calculate_total(scores):
    return sum(scores)


def calculate_average(scores):
    return statistics.mean(scores)


def find_maximum(scores):
    return max(scores)


def find_minimum(scores):
    return min(scores)


student = {
    "name": "christopher",
    "scores": [80, 80, 70, 100, 50, 90, 70]
}


scores = student["scores"]
print("==========================================")
print("Name:", student["name"])
print("Total:", calculate_total(scores))
print("Average:", calculate_average(scores))
print("Maximum:", find_maximum(scores))
print("Minimum:", find_minimum(scores))
