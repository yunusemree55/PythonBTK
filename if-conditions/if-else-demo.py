"""
name = input("İsim: ")
age = int(input("Yaş: "))
education = input("Eğitim Durumu: ")

if(age >= 18):
    if(education == "Lise" or education == "Üniversite"):
        print("Ehliyet Alabilir")
    else:
        print("Ehliyet almak için eğitim seviyesi yetersiz")
else:
    print("Ehliyet almak için en az 18 yaşında olmalısınız")

"""

# -------------------------------------------------------------------


"""
exam1 = int(input("Not-1 : "))
exam2 = int(input("Not-2 : "))
speaking = int(input("Sözlü: "))

result = (exam1 + exam2 + speaking) / 3

if( 0<=result <=24):
    print("Karne notu: 0")
elif( 25<= result <=44):
    print("Karne notu: 1")
elif( 45<= result <=54):
    print("Karne notu: 2")
elif( 55<= result <=69):
    print("Karne notu: 3")
elif( 70<= result <=84):
    print("Karne notu: 4")
elif( 85<= result <=100):
    print("Karne notu: 5")

"""

# -------------------------------------------------------------------