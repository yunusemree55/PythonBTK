
number = int(input("Sayı giriniz: "))

sayac = 1

while sayac <= number:
    
    if( (sayac == number) % number == 0 ):
        print(f"{number} asal sayıdır")
    else:
        print(f"{number} asal sayı değildir")
    
    sayac += 1

