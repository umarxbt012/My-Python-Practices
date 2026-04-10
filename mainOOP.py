#using claude as learning material
class Dog:
    def __init__(self, name, breed, age):
        self.name=name
        self.breed=breed
        self.age=age
        self.tricks=[]
        
    def learnTrick(self,trick):
        self.tricks.append(trick)
        
    def learnTricks(self,tricks):
        self.tricks.extend(tricks)
    
    def learnMany(self,*tricks):
        self.tricks.extend(tricks)
    
    def showTrick(self):
        if self.tricks:
            print(f"{self.name} has learnt the following tricks: {",".join(self.tricks)}")
        else:
            print(f"{self.name} has not learned any tricks")
            
    def describe(self):
        print(f"{self.name} is a {self.breed} breed and is {self.age} years old.")
        
    def ispuppy(self):
        return self.age>2

#you can check the various methods such as learnTrick, learnTricks and learnMany
dog1=Dog("alex", "labrador", 3)
dog1.describe()
print(dog1.ispuppy())
dog1.learnMany("sit","Roll On")
dog1.showTrick()











        