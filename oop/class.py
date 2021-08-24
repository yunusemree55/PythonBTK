# Class

class Person:


    
    # class attributes
    address = "No information"
    # constructor (yapıcı metot)
    def __init__(self,name,year):
         # object attributes
        self.name = name
        self.year = year
    

    #instance methods

    def intro(self):
        print("Hello there " + self.name)

    #instance methods

    def calculateAge(self):
        return 2021 - self.year


# object (instance)
p1 = Person(name = "Yunus",year = 2001)
p2 = Person("Enes",2003)

# updating
p1.name = "Emre"
p2.address = "Bursa"


# print(f"name: {p1.name} , birthday: {p1.year}, address: {p1.address}")
# print(f"name: {p2.name} , birthday: {p2.year}, address: {p2.address}")

# print(p1)
# print(p2)

# print(type(p1))
# print(type(p2))


# p1.intro()
# p2.intro()

# print(f"I'm {p1.name} and {p1.calculateAge()} years old")
# print(f"I'm {p2.name} and {p2.calculateAge()} years old")


class Circle:

    # Class object attribute
    pi = 3.14

    def __init__(self,r = 1):
        self.r = r

    # Methods

    def circumference(self):
        return 2*self.pi * self.r 
    
    def area(self):
        return self.pi * (self.r**2)


c1 = Circle() # r = 1
c2 = Circle(5)

print(f"c1 area : {c1.area()}\nc1 circumference : {c1.circumference()}")
print(f"c2 area : {c2.area()}\nc2 circumference : {c2.circumference()}")

