from lib.student import Student

student = Student(1, "Student Test", 2)

"""
Student constructs with an id, name and cohort_id
"""

def test_student_constructs():
    assert student.id == 1
    assert student.name == "Student Test"
    assert student.cohort_id == 2

"""
We can format student strings nicely
"""

def test_student_formats_nicely():
    assert str(student) == "Student(1, Student Test, 2)"

"""
We can comparte two identical students 
And have them to be equal
"""

def test_students_are_equal():
    student2 = Student(1, "Student Test", 2)
    assert student2 == student