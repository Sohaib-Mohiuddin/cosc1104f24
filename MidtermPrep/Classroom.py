import numpy as np

class Classroom:
    def __init__(self):
        self.students = []
    
    def class_avg(self):
        class_grades = [student.avg_grade() for student in self.students]
        return np.mean(class_grades)
    
    def add_student(self, student):
        self.students.append(student)
    
    # Find the top student with the help of the max() function