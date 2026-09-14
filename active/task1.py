import statistics

scores = [50, 60, 70, 80, 90, 40]

print("Sum:", sum(scores))
print("Mean:", statistics.mean(scores))
print("Median:", statistics.median(scores))
print("Mode:", statistics.multimode(scores))
print("Variance:", statistics.variance(scores))
print("Standard deviation:", statistics.stdev(scores))
