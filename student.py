class Student:
    counter = 0
    def __init__(self,name,id,grades=None):
        self.name=name
        self.id=Student.counter
        Student.counter+=1
        self.grades= grades if not None else []
    
    def addGrade(grade):
        self.grades.append(grade)
        
