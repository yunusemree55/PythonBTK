
sayilar = [1,3,5,7,9,12,19,21]

i = 0
# while i < len(sayilar):
#     print(sayilar[i])
#     i += 1


# ilk = int(input("ilk sayı: "))
# son = int(input("son sayı: "))



# while ilk < son:
#     print(ilk)
#     ilk += 1


i = 100
# while i >= 0:
#     print(i)
#     i -= 1


value = int(input("ürün sayısı : "))

while value > 0:
    name = input("ürün ismi: ")
    price = input("fiyatı: ")
    urunler = {
        'name' : name , 'price' : price
    }
    value -= 1

for urun in urunler:
    print(urun["name"])
