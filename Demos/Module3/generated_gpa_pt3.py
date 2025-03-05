"""
This test code was generated from a request interacting with openAI API libraries in part3() of generate_students_report.py
Instructions were to create the code with dictionary comprehension and formatted for readability
"""
student_data = {101: {"name": "Alice", "grades": [85, 90, 92, 88], "gpa": round(sum([85, 90, 92, 88]) / len([85, 90, 92, 88]) / 25, 2)},
 102: {"name": "Bob", "grades": [78, 82, 80, 85], "gpa": round(sum([78, 82, 80, 85]) / len([78, 82, 80, 85]) / 25, 2)},
 103: {"name": "Charlie", "grades": [92, 94, 90, 88], "gpa": round(sum([92, 94, 90, 88]) / len([92, 94, 90, 88]) / 25, 2)}}

for student_id, student_info in student_data.items():
    print(f"Student ID: {student_id}")
    print(f"Name: {student_info['name']}")
    print(f"Grades: {student_info['grades']}")
    print(f"GPA: {student_info['gpa']}")
    print()