import numpy as np

# Define student class
class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def avg_grade(self):
        np.mean(self.grades)
    
    def display_info(self):
        return f'Student: { self.name }, Age: { self.age }, Grades: { self.grades }'