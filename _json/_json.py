import json


person_string = '{"name" : "Yunus Emre", "languages": ["python","C#"]}'

# JSON string to Dict

# result = json.loads(person_string)
# result = result["name"]

# with open("person.json","r") as f:
#     data = json.load(f)
#     print(data)
#     print(data["name"])



#  Dict to JSON string 

person_dict = {
    "name": "Raymond",
    "languages": ["Python","C#"]


}

# result = json.dumps(person_dict)

# print(result)
# print(type(result))



# with open("person.json","w") as f:
#     json.dump(person_dict,f)


person_dict = json.loads(person_string)

result = json.dumps(person_dict,indent= 4,sort_keys=True)
print(person_dict)
print(result)





