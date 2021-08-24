
names = ["Ali", "Yağmur","Hakan","Deniz"]
years = [1998,2000,1998,1987]

names.append("Cenk")
names.insert(0,"Sena")
# names.remove("Deniz")
value = names.count("Ali")
names.reverse()
names.sort()
print(names)
print(value)

years.sort()
years.reverse()
print(years)

str = "Chevrolet , Dacia"
str = [str]
print(str)

val = max(years)
val = min(years)
val = years.count(1998)
print(val)
years.clear()
print(years)

car1 = input("1)Araba ismi: ")
car2 = input("2)Araba ismi: ")
car3 = input("3)Araba ismi: ")

cars = [car1,car2,car3]
print(cars)
