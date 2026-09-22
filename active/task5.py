def passing_scores(scores):
    passed = []
    for index in range(len(scores)): # the loop stops exactly one item short of the end of the list.
        if scores[index] > 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))



def passing_scores(scores):
    passed = []
    for score in scores:  # Loops through every score directly
        if score > 50:   # Keeps 50 and above
            passed.append(score)
    return passed

print(passing_scores([49, 50, 80, 65]))  # Output: [50, 80, 65]
