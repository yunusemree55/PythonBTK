import random

randomiseNumber = random.randrange(1,15)
hak = 5


while True:
    tahmin= int(input("Tahmin: "))
    hak -= 1
    if(hak == 0):
        print(f"Tahmin hakkınız kalmadı\n\n\nDoğru cevap: {randomiseNumber}")
        break
    elif(tahmin > randomiseNumber):
        print(f"\nAşağı\nKalan tahmin hakkı: {hak}")
    elif(tahmin < randomiseNumber):
        print(f"\nYukarı\nKalan tahmin hakkı: {hak}")
    else:
        print(f"\nTahmin edilen sayı: {randomiseNumber}\nTahmininiz: {tahmin}\nKalan Hakkınız: {hak}")
        break



