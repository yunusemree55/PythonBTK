import sys

liste = [7,"Yunus",0,3,"6"]

for x in liste:
    try:
        print("Sonuç:" , 1/int(x))
    except ValueError:
        print(f"{str(x)} bir sayı değil")
    except ZeroDivisionError:
        print(f"{str(x)} için sıfıra bölme hatası")
    except:
        print(f"{str(x)} hesaplanamadı")
        print(f"Sistem hatası: {sys.exc_info()[0]}")
    finally:
        print("İşlemler bitti")
   






















