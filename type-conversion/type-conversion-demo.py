
r = float(input("Dairenin yarıçapını giriniz: "))
selection = int(input("Daire Alanı hesaplaması: 1 \nDaire Çevresi hesaplaması: 2\nSeçenek: "))

if(selection == 1):

    result = 3.14 * r**2
    print("Daire Alanı: " + str(result))

elif(selection == 2):

    result = 2*3.14*r
    print("Daire Çevresi: " + str(result))
else:
    print("Geçerli sayı giriniz")



