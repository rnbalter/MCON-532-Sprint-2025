students = {
"123": {"name": "Alice", "grades": [80, 85, 90], "gpa": round(sum([80, 85, 90]) / len([80, 85, 90]) / 25, 2)},
"234": {"name": "Bob", "grades": [75, 80, 85], "gpa": round(sum([75, 80, 85]) / len([75, 80, 85]) / 25, 2)},
"345": {"name": "Charlie", "grades": [85, 90, 95], "gpa": round(sum([85, 90, 95]) / len([85, 90, 95]) / 25, 2)}}

# Using dictionary comprehension
student_ids = ["123", "234", "345"]

student_data = {sid: {"name":  students[sid]["name"], "grades":  students[sid]["grades"], "gpa":  students[sid]["gpa"]}
            for sid in student_ids}
print(student_data)

