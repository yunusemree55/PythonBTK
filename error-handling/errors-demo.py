
liste = ["1","2","5a","10b","abc","10","50"]



numbers = []

for x in liste:
    try:
        numbers.append(int(x))
    except:
        print("Sayısal değer içermiyor")

print(numbers)

# --------------------------------------------------

# %%


while True:
    choice = input("Devam etmek istiyor musunuz (d/q)? : ")
    if(choice == "d"):
        try:
            number = int(input("Sayı giriniz: "))
        except ValueError:
            print("Tip uyuşmazlığı: Lütfen sayı tipinde değer giriniz")

    else:
        break
    
# %%    

password = input("Şifre giriniz: ")

turkishLetter = "ığüçöİĞÜÇşŞ"

for x in password:
    if x in turkishLetter:
        raise TypeError("Türkçe Karakter içermemeli")
    else:
        pass

print("Şifre kabul edildi")    


# %%

def checkNumber(number):
    try:
        if(int(number) == True):
            pass
    except TypeError:
        print("Yanlış tip girdiniz: Sayı değer giriniz")
        


def factorial(number):
    result = 1
    try:
        for x in range(1,number+1):
            result *= x

        print("{}! = {}".format(number,result))
    except:
        print("HATA")


   
checkNumber("ab")  
   

factorial(6)
print("BİTTİ") 

   









# %%
