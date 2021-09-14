# try:
#     file = open("newfile2.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya okuma hatası")
# finally:
#     file.close()
#     print("Dosya kapandı")

file = open("newfile.txt","r",encoding="utf-8")


# ************ for döngüsü

# for x in file:
#     print(x, end="")

# ************ read() fonksiyonu

# content1 = file.read()
# print("içerik 1")

# print(content1)

# content2 = file.read()

# print("içerik 2")
# print(content2)

# file.close()


# content = file.read(5)
# content = file.read(3)
# print(content)

# file.close()


# ********* readline() fonksiyonu

# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# print(file.readline())

# file.close()


# ********* readlines() fonksiyonu

liste = file.readlines()

print(liste)

print(liste[0])
print(liste[1])
print(liste[2])


file.close()

