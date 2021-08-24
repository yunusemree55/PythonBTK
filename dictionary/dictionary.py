# key - value

sehirler = ["Kocaeli","İstanbul"]
plakalar = [41,34]

# dictionary {"key" : "value"}

plakalar = {"Kocaeli" : 41 , "İstanbul" : 34}

# print(plakalar["Kocaeli"])
# print(plakalar["İstanbul"])

plakalar["Ankara"] = 6
# plakalar["Kocaeli"] = "New Value"

# print(plakalar)

users = {
    "Yunus Emre Çiçek" : {
        "age":20,
        "roles" : ["admin","user"],
        "mail": "emre@gmail.com",
        "address" : "Bursa",
        "phone":"12345"
    },
    "Enes Emir Çiçek" : {
        "age":18,
        "roles" : ["user"],
        "mail": "enes@gmail.com",
        "address": "Bursa",
        "phone":"98765"
    }
}

print(users["Yunus Emre Çiçek"]["roles"][0])