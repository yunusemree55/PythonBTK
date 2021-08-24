
sayilar = [1,3,5,7,9,12,19,21]

# for x in sayilar:
#     if(x % 3 == 0):
#         print(x)


# result = 0
# for x in sayilar:
#     result += x
# print(result)

# for x in sayilar:
#     if(x % 2 !=0):
#         print(x**2)


sehirler = ["Kocaeli","İstanbul","Ankara","İzmir","Rize"]

# for sehir in sehirler:
#     if(len(sehir) <= 5):
#         print(sehir)


urunler = [
    {"name": "samsung S6","price" : "3000"},
    {"name": "samsung S7","price" : "4000"},
    {"name": "samsung S8","price" : "5000"},
    {"name": "samsung S9","price" : "6000"},
    {"name": "samsung S10","price" : "7000"}
]

total = 0

for urun in urunler:
    total += int(urun["price"])

print(total)


for urun in urunler:
    if(int(urun["price"]) <=5000):
        print(urun)