"""
This test code was generated from a request interacting with openAI API libraries in part4() of generate_students_report.py

These unittests confirm that:
there are 3 students,
that each student has a name, grades, and gpa
that the grades are all int type only
"""
import unittest

#To run this unittest on the third generated code:
#from Demos.Module3.generated_gpa_pt3 import student_data

student_data = {
    1: {"name": "Alice", "grades": [85, 90, 88], "gpa": round(sum([85, 90, 88])/len([85, 90, 88])/25, 2)},
    2: {"name": "Bob", "grades": [75, 80, 82], "gpa": round(sum([75, 80, 82])/len([75, 80, 82])/25, 2)},
    3: {"name": "Charlie", "grades": [90, 95, 92], "gpa": round(sum([90, 95, 92])/len([90, 95, 92])/25, 2)}  }

class TestStudentDictionary(unittest.TestCase):
  def test_number_of_student_data(self):
      self.assertEqual(len(student_data), 3)

  def test_student_details(self):
      for student_id, student_info in student_data.items():
          self.assertIn("name", student_info)
          self.assertIn("grades", student_info)
          self.assertIn("gpa", student_info)

  def test_grade_type(self):
      for student_id, student_info in  student_data.items():
          self.assertTrue(all(isinstance(grade, int) for grade in
student_info["grades"]))

if __name__ ==  '__main__'   :
  unittest.main()


