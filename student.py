class Student:
    counter = 1
    def __init__(self,name,grades=None):
        self.name=name
        self.id=Student.counter
        Student.counter+=1
        self.grades= grades if grades is not None else []
    
    def addGrade(self):
        grade=int(input(f"Enter the score of {self.name}: "))
        self.grades.append(grade)
        print(f"{grade} has been added to {self.name}")
        
    def calcGrade(self):
        sum=0
        for i in range(len(self.grades)):
            sum+=self.grades[i]
        print(f"the total score of {self.name} is : {sum}")
        
    def averageScore(self):
        if len(self.grades)==0:
            print("No grades have been inputted")
            return
        sum =0
        for i in range(len(self.grades)):
            sum+=self.grades[i]
        average= sum/len(self.grades)
        print(f" the average of {self.name} scores is: {average}")
    
    def highestScore(self):
        maxNum=self.grades[0]
        for i in range(len(self.grades)):
            if self.grades[i]>maxNum:
                maxNum=self.grades[i]
        print(f"the maximum score of {self.name}'s score is {maxNum}")
    
    def lowestScore(self):
        minNum=self.grades[0]
        for i in range(len(self.grades)):
            if self.grades[i]<minNum:
                minNum=self.grades[i]
        print(f"the lowest score of {self.name}'s score is {minNum}")
                
    def display(self):
        formattedId=str(self.id).zfill(4)
        formattedName=self.name.title()
        print(f"ID:{formattedId}")
        print(f"NAME:{formattedName}")
        print(f"GRADES:{self.grades}")
        
s1=Student("Faruk")
s1.addGrade()
s1.addGrade()
s1.addGrade()
s1.calcGrade()
s1.averageScore()
s1.highestScore()
s1.lowestScore()
s1.display()
s2 = Student("Aisha")
s2.addGrade()
s2.addGrade()
s2.addGrade()
s2.calcGrade()
s2.averageScore()
s2.highestScore()
s2.lowestScore()
s2.display()
