"""
ogrenciler = {

    "120" : {
        "name" : "Ali",
        "surname" : "Yılmaz",
        "telephone" : "532 000 00 01"
    },
    "125" : {
        "name" : "Can",
        "surname" : "Korkmaz",
        "telephone" : "532 000 00 02"
    },
    "128" : {
        "name" : "Volkan",
        "surname" : "Yükselen",
        "telephone" : "532 000 00 03"
    },
}
"""

schoolNumber1 = input("Okul numarası: ")
name1 = input("İsim: ")
surname1 = input("Soyisim: ")
phone1 = input("Telefon numarası: ")

schoolNumber2 = input("Okul numarası: ")
name2 = input("İsim: ")
surname2 = input("Soyisim: ")
phone2 = input("Telefon numarası: ")

schoolNumber3 = input("Okul numarası: ")
name3 = input("İsim: ")
surname3 = input("Soyisim: ")
phone3 = input("Telefon numarası: ")

students = {

    schoolNumber1 : {
        "name" : name1,
        "surname": surname1,
        "phone" : phone1
    },
     schoolNumber2 : {
        "name" : name2,
        "surname": surname2,
        "phone" : phone2
    },
     schoolNumber3 : {
        "name" : name3,
        "surname": surname3,
        "phone" : phone3
    },

}

print(students)

value = input("Öğrenci numarası giriniz: ")
print(students[value])

