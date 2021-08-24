"""
a = int(input("sayı-1 : "))
b = int(input("sayı-2 : "))

if(a>b):
    print(f"En büyük sayı {a}")
elif(b>a):
    print(f"En büyük sayı {b}")
else:
    print("İki sayı birbirine eşittir")
"""

#-----------------------------------------------#

"""
midTerm1 = int(input("Vize1 notu: "))
midTerm2 = int(input("Vize1 notu: "))
final = int(input("Final notu: "))

result = ((midTerm1 + midTerm2) * 60/100) + (final * 40/100)

if(result >= 50):
    print("Başarılı")
else:
    print("Başarısız")
"""

#-----------------------------------------------#

"""
number = int(input("Sayı giriniz : "))

if(number % 2 == 0):
    print("Girilen sayı ÇİFTTİR")
else:
    print("Girilen sayı TEKTİR")


if(number < 0):
    print("Girilen sayı NEGATİFTİR")
elif(number > 0 ):
    print("Girilen sayı POZİTİFTİR")
else:
    print("Girilen sayı ne Pozitif ne Negatiftir")
"""

#-----------------------------------------------#

email, password = "abcd@gmail.com", "abc123"

e1 = input("Email adresi: ")
p1 = input("Şifre: ")

if(e1 == email and p1 == password):
    print("Giriş Başarılı")
else:
    print("Giriş Başarısız")