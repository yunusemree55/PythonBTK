class Matematik:

    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
        pass

    def topla(self):
        return self.number1 + self.number2
    def cikar(self):
        if(self.number1 > self.number2):
            return self.number1 - self.number2
        else:
            return self.number2 - self.number1
    
    def carpma(self):
        return self.number1 * self.number2
    
    def bolme(self):
        if(self.number1> self.number2):
            return self.number1 / self.number2
        else:
            return self.number2 / self.number1


hesapla = Matematik(5,9)

result = hesapla.topla()
print(result)

result = hesapla.cikar()
print(result)

result = hesapla.carpma()
print(result)

result = hesapla.bolme()
print(result)


# %%

class Person:
    def __init__(self,firstName,lastName,age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

class Worker(Person):
    def __init__(self,salary,department):
        self.salary = salary
        self.department = department

class Customer(Person):
    def __init__(self,creditCard):
        self.creditCard = creditCard
        

worker1 = Worker(5000,"IT")

worker1.firstName = "Yunus Emre"
worker1.lastName = "Çiçek"
worker1.age = 20


print(worker1.firstName)
print(worker1.department)
