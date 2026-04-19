#beginning object oriented programming in python
class Car:
    def __init__(self,brand,color,make, speed=0,fuel=100):
        self.brand=brand
        self.color=color
        self.make=make
        self.speed=speed
        self.fuel=fuel
    #do a drive method, accelerate deccelerate, refuel 
    def drive(self):
        print(f"{self.brand} has started")
    def accelerate(self):
        if self.fuel<=0:
            print("no fuel")
            return
        #the prescence of return exits the method immediately
        self.speed+=10
        if self.speed>100:
            self.speed=100
        self.fuel=max(0,self.fuel-1)
        print(f"{self.brand} is at a speed of {self.speed} and fuel amount is now {self.fuel}.")
    def deccelerate(self):
        self.speed-=10
        if self.speed <= 0:
            self.speed=0
        print(f"{self.brand} has deccelerated by 10 and speed now is {self.speed} ")
        if self.speed==0:
            print(f"{self.brand} has stopped!")
            return
            
    def refuel(self,amount):
        maxFuel=100
        needed_fuel=maxFuel-self.fuel
        if amount>needed_fuel:
            change=amount-needed_fuel
            self.fuel=maxFuel
            print(f"it has exceeded the fuel needed here is your change:{change} ")
        else:
            self.fuel+=amount
            change=0
            print("fuel refilled. no change")
        print(f"You have refueled your {self.brand} by {needed_fuel} and now fuel amount is now {self.fuel}")
    def display(self):
        print("THIS IS THE INFORMATION ABOUT YOUR CAR")
        print(f"BRAND: {self.brand}")
        print(f"COLOR: {self.color}")
        print(f"MAKE: {self.make}")
        print(f"SPEED: {self.speed}")
        print(f"FUEL AMOUNT: {self.fuel}")

car1=Car("toyota","red","2007")
car1.accelerate()
car1.deccelerate()
car1.refuel(20)
car1.display()
car2=Car("Ferrari","Indigo","2023")
car2.accelerate()
car2.deccelerate()
car2.refuel(20)
car2.display()