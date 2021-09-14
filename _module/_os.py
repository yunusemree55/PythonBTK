import os

# result = dir(os)


result = os.name
# etkin dizin gösterme
result = os.getcwd()

# Dizin değiştirme
# os.chdir('C:\\')
result = os.getcwd()

# Klasör oluşturma
# os.mkdir("newdirectory")
# os.makedirs("newdirectory/yeniklasor")

#  listeleme
# result = os.listdir()
# result = os.listdir("C:\\")

for dosya in os.listdir():
    if dosya.endswith(".py"):
        print(dosya)


print(result)