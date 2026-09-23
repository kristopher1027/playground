Day 2 Python Core Engineering Assessment
etzkristokency2@gmail.com Switch account
 
Question 2 Find the missing passes
Easy to moderate  |  9 minutes  |  15 marks
Return every score greater than or equal to 50, in the original order. Inputs are lists of integers from 0 to 100. An empty list must return an empty list.
def passing_scores(scores):
    passed = []
    for index in range(len(scores) - 1):
        if scores[index] > 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))
Q2 Part B
Correct the function without changing the input list. [6 marks]
def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed
print(passing_scores([49, 50, 80, 65]))
Q2 Part A
Predict the current printed output. Identify both independent defects and explain which result each defect loses. [5 marks]
[80]

1. (range(len(scores) - 1)): The loop stops early and completely skips checking the very last item in the list. 
2. Wrong comparison operator (scores[index] > 50)
Q2 Part C
Write three executable assertions: one for the pass boundary 50, one for a single passing score, and one for an empty list. [4 marks]
# 1. Pass boundary 50 
assert passing_scores([49, 50, 51]) == [50, 51]

# 2. Single passing score
assert passing_scores([20, 85, 30]) == [85]

# 3. Empty list
assert passing_scores([]) == []
