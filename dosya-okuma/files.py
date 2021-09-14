# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adı,dosya_erişim_modu)
# dosya_erişim_modu => dosyayı hangi amaçla açtığımızı belirtir

# "w": (Write) yazma modu. Dosyayı konumda oluşturur
#       ** Dosyayı konumda açar
#       ** Dosya içeriğini siler ve yeniden ekleme yapar

# file = open("newfile.txt","w")
# file = open("C:/Users/Yunus Emre/Desktop/newfile.txt","w")
# file.close()

# file = open("newfile.txt","w",encoding="utf-8")
# file.write("Türkiye")
# file.close()



# "a": (Append) ekleme. Dosya konumda yoksa oluşturur

# file = open("newfile.txt","a",encoding="utf-8")
# file.write("Matematik\n")
# file.close()




# "x": (Create) oluşturma. Dosya zaten varsa hata verir

# file = open("newfile2.txt","x",encoding="utf-8")



# "r": (Read) okuma. varsayılan. Dosya konumda yoksa hata verir