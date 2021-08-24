
def sayHello(user = "user"):
   return "Hello " + user

msg = sayHello("Yunus")
print(msg)


def total(num1,num2):
    return num1 + num2

result = total(5,4)
print(result)


def yasHesapla(dogumYili):
    return 2021 - dogumYili

result = yasHesapla(2001)
print(result)

def emekliligeKacYilKaldi(dogumYili,isim):
    """
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if(emeklilik > 10):
        print(f"emekliliğinize {emeklilik} yıl kaldı")
    else:
        print("Zaten emekli oldunuz")

emekliligeKacYilKaldi(2001,"Yunus Emre")
help(emekliligeKacYilKaldi)