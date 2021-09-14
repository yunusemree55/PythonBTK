
hesapA = {
    "ad" : "Yunus Emre Çiçek",
    "hesapNo" : "13245678",
    "bakiye" : 3000,
    "ekHesap" : 2000
}

hesapB = {
    "ad" : "Ahmet Turan",
    "hesapNo" : "13245678",
    "bakiye" : 2000,
    "ekHesap" : 1000
}


def paraCek(hesapAdı,miktar=0):
    
    print(f"Merhaba {hesapAdı['ad']}")

    if(miktar > hesapAdı['bakiye'] + hesapAdı['ekHesap']):
      print("Hesaplarınızdaki miktarlar yetersiz")
      return  

    elif(miktar > hesapAdı['bakiye']):
        secim = input("Ek hesaptan da para çekilsin mi?\n")
        if(secim == "Evet" or secim == "evet"):
            total = hesapAdı['bakiye'] + hesapAdı['ekHesap'] - miktar


        else:
            return  
    hesapAdı['bakiye'] -= miktar
    print(f"{hesapAdı['hesapNo']} no'lu hesabınızdan {miktar} çekilmiştir")


        




paraCek(hesapA,2000)
paraCek(hesapA,2000)