import requests


class Github:
    def __init__(self) -> None:
        self.api_url = "https://api.github.com"
    
    def getUser(self,username):
        response = requests.get(self.api_url + "/users/" + username)
        return response.json()
    
    def getRepository(self,username):
        response = requests.get(self.api_url + "/users/" + username + "/repos")
        return response.json()

github = Github()

while True:
    print("Menü".center(50,"*"))
    option = input("1-Find User\n2-Find Repositories\n3-Exit\nSeçim: ")

    if option == "3":
        break
    else:
        if option == "1":
            username = input("Username: ")
            result = github.getUser(username)
            print(f'GitHub Name: {result["login"]}  Name = {result["name"]} followers: {result["followers"]}')
        elif option == "2":
            username = input("Username: ")
            result = github.getRepository(username)
            for repo in result:
                print(f'name: {repo["name"]} full_name: {repo["full_name"]}  ')

        else:
            print("Hatalı Seçim")












