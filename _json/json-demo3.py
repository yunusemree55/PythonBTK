import json
import os


class User:
    def __init__(self,username,password, email) -> None:
        self.username = username
        self.password = password
        self.email = email

class UserRepository:
    def __init__(self) -> None:
        self.users = []
        self.isLoggedIn = False
        self.currentUser = {}

        # load users from .json file
        self.loadUser()

    def loadUser(self):
        pass

    def register(self,user:User):
        self.users.append(user)
        self.saveToFile()
        print("Kullanıcı oluşturuldu")

    def login(self):
        pass

    def saveToFile(self):
        
        list = []
        for user in self.users:
            list.append(json.dumps(user.__dict__))

        with open("users2.json","w",encoding="utf-8") as file:
            json.dump(list,file)



repository = UserRepository()

while True:

    print("Menü".center(50,"*"))
    secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nSeçiminiz: ")
    
    if secim == "5":
        break
    else:
        if secim == "1":    #Register
            username = input("username: ")
            password = input("password: ")
            email = input("email: ")

            user = User(username= username,password= password,email= email)
            repository.register(user)
            
            print(repository.users)

        elif secim == "2":  #Login
            pass
        elif secim == "3":  #Logout
            pass
        elif secim == "4":  #Identity
            pass
        else:
            print("Yanlış Seçim")









































