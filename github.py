import requests

class Github:
    def __init__(self) -> None:
        self.api_url = "https://api.github.com"

    def getUser(self,username):
        response = requests.get(self.api_url + "/users/" + username)
        
        return response.json()
    
    def getRepository(self,username):
        respond = requests.get(self.api_url + "/users/" + username + "/repos")
        return respond.json()


github = Github()

while True:
    secim = input("1-Find User\n2-Get Repository\n3-Exit\nSeçim: ")

    if secim == "3":
        break
    else:
        if secim == "1":
            username = input("username: ")
            result = github.getUser(username)
            print(f'name: {result["name"]} public repos: {result["public_repos"]} followers: {result["followers"]}')
        elif secim == "2":
            username = input("username: ")
            result = github.getRepository(username)
            for repo in result:
                print(f'name: {username} repos_name = {repo["name"]}')
        else:
            print("Yanlış Seçim")


