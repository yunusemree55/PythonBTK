
customerName = "Yunus Emre"
customerLastName = " Çiçek"

customer = customerName + customerLastName

customerGender = "Erkek"
customerIdentityNumber = "12345678910"
customerAddress = "Bursa"
customerAge = 20 



x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# n1 = int(input("sayı-1 : "))
# n2 = int(input("sayı-2 : "))

# total = n1*n2 - (x+y+z)

# print("İşlem sonucu: {}".format(total))


# result = y // x
result = (x+y+z) % 3
result = y**x

x,*y,z = numbers

result = z**3
result = y[0] + y[1] + y[2]

# print(result)

"""

number = int(input("Sayı giriniz: "))

if(0< number <100):
    print("Sayı 0-100 arasındadır")
else:
    print("Sayı 0-100 arasında değildir")


number = int(input("Sayı giriniz: "))

if(number > 0 and number % 2 == 0):
    print("Girilen sayı POZİTİF ve ÇİFT SAYIDIR")
else:
    print("HATA")
"""

#--------------------------------------------------#

"""
a = int(input("Sayı1: "))
b = int(input("Sayı2: "))
c = int(input("Sayı3: "))

if(a>b and a>c and b>c):
    print(f"{a} > {b} > {c}")
elif(a>b and a>c and c>b):
    print(f"{a} > {c} > {b}")
elif(b>a and b>c and a>c):
    print(f"{b} > {a} > {c}")
elif(b>a and b>c and c>a):
    print(f"{b} > {c} > {a}")
elif(c>a and c>b and a>b):
    print(f"{c} > {a} > {b}")
elif(c>a and c>b and b>a):
    print(f"{c} > {b} > {a}")

"""

#--------------------------------------------------#

height = float(input("Boy: "))
weight = int(input("Kilo: "))

result = weight / height**2

if(0<result<18.4):
    print("ZAYIF")
elif(18.5<result<24.9):
    print("Normal")
elif(25.0<result<29.9):
    print("Normal")
elif(30.0<result<34.9):
    print("Normal")