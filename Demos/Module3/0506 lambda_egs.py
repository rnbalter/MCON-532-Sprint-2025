'''
A lambda function is a concise, anonymous function defined with the lambda keyword.
It's often used for short operations that are passed as arguments to functions like map(), filter(), or sorted().

lambda arguments: expression
arguments: one or more parameters (comma-separated if multiple)
expression: a single return value (no return keyword)
'''

square = lambda x: x * x
print(square(5))  # Output: 25

add = lambda x, y: x + y
print(add(3, 4))  # Output: 7

print((lambda x: x**2)(6))  # Output: 36

'''
lambda is for simple, single-expression functions.
It cannot contain multiple statements, assignments, or loops.
You don’t use def, return, or even a name—unless assigning to a variable.
'''

names = ['alice', 'bob', 'carol']
name_lengths = {name: (lambda x: len(x))(name) for name in names}
# Output: {'alice': 5, 'bob': 3, 'carol': 5}
print(name_lengths)


nums = [1, 2, 3, 4, 5, 6]
even_nums = list(filter(lambda x: x % 2 == 0, nums))
# Output: [2, 4, 6]
print(even_nums)

grades = {'Alice': 85, 'Bob': 72, 'Carol': 90}
high_achievers = {k: v for k, v in grades.items() if (lambda score: score > 80)(v)}
# Output: {'Alice': 85, 'Carol': 90}
print(high_achievers)


students = [('Alice', 85), ('Bob', 72), ('Carol', 90)]
sorted_students = sorted(students, key=lambda x: x[1])
# Output: [('Bob', 72), ('Alice', 85), ('Carol', 90)]
print(sorted_students)

grades = {'Alice': 85, 'Bob': 72, 'Carol': 90}
sorted_by_score = dict(sorted(grades.items(), key=lambda x: x[1]))
# Output: {'Bob': 72, 'Alice': 85, 'Carol': 90}
print(sorted_by_score)

