# 1. Use lambda with dictionary comprehension to map names to name lengths
names = ['david', 'lila', 'miriam', 'chana']
name_lengths = {
    name: (lambda x: len(x))(name) for name in names
    #why is this not then (lambda x: len(x), name) for name in names??
    #doing so causes chaos and says "{'Eli': <filter object at 0x000001CADB7BBE50>..." hmmmm
}
print("Name lengths:", name_lengths)

# 2. Filter a list to keep only numbers divisible by 3
numbers = list(range(1, 20))
divisible_by_3 = list(
    filter(lambda x: x%3 == 0, numbers)
)
print("Divisible by 3:", divisible_by_3)

# 3. Filter a dictionary to keep only values > 75
scores = {'Eli': 88, 'Sara': 74, 'Mo': 91, 'Rachel': 68}
high_scores = {
    hs: scores for hs, scores in scores.items() if (lambda x: x>75)(scores)
    #hs: hs for scores, hs in scores.items() if (lambda score: score>75)(hs)
    #this gives "High scores: {88: 88, 91: 91}" bc i mapped it incorrectly ie order in the loop rlly matters
}
    #hs: filter(lambda x: x>75, hs) for hs in scores}
    #this gives the filter obj same as #1 error - why do we have to reverse the syntax order here?
print("High scores:", high_scores)

# 4. Sort a list of (name, age) tuples by age
people = [('Eli', 28), ('Sara', 21), ('Mo', 35), ('Rachel', 25)]
sorted_people = sorted(
    people, key = lambda x: x[1]
)
print("Sorted people by age:", sorted_people)

# 5. Sort dictionary entries by value (descending)
grades = {'Eli': 88, 'Sara': 74, 'Mo': 91, 'Rachel': 68}
sorted_grades = dict(
    sorted(grades.items(), key = lambda x: x[-1])
)
print("Grades sorted:", sorted_grades)