
# def changeName(n):

#     n = "Yeni İsim"

# name = "Yunus"

# changeName(name)
# print(name)

# def change(n):
#     n[0] = "İstanbul"

# sehirler = ["Ankara", "İzmir"]

# change(sehirler)
# print(sehirler)


# def add(*params):
#     return sum((params))

# result = add(5,3,50,80,45,-80,66,52,10)
# print(result)

def displayUser(**args):
    print(type(args))
    for key,value in args.items():
        print(f"{key} is {value}")

displayUser(name = "Yunus Emre", age= 20, city = "Bursa")
displayUser(name = "Enes Emir", age= 18, city = "Bursa")
displayUser(name = "Furkan", age= 20, city = "Bursa")


def myFunc(a,b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

myFunc(10,20,30,40,50, key1 = "value1" , key2 = "value2")