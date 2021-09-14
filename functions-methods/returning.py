
# def usAlma(number):

#     def inner(power):
#         return number**power
    
#     return inner


# five = usAlma(5)
# print(five(2))

# ten = usAlma(10)
# print(ten(2))


# def yetki_sorgula(page):
#     def inner(role):
#         if role == "Admin":
#             return f"{role} rolü {page} sayfasına ulaşabilir"
#         else:
#             return  f"{role} rolü {page} sayfasına ulaşamaz"
#     return inner


# user1 = yetki_sorgula("Product Edit")
# user2 = yetki_sorgula("Product Edit")

# print(user1("Admin"))
# print(user2("User"))


# def islem(islem_adi):
#     def toplam(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam

#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim *= i
#         return carpim

#     if islem_adi == "toplama":
#         return toplam
#     if islem_adi == "çarpma":
#         return carpma

# toplama = islem("toplama")
# print(toplama(3,5,9,10,-8))

# carpma = islem("çarpma")
# print(carpma(3,8,4,-1))


def selamla(user_type):

    def admin(name):
        return f"Hoşgeldin Kurucu {name}"
    
    def user(name="ziyaretçi"):
        return f"Merhaba {name}"

    if user_type == "admin":
        return admin
    if user_type == "user":
        return user



user1 = selamla("admin")

print(user1("Yunus Emre"))

user2 = selamla("user")
print(user2())




