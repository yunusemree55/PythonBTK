import json

data = '{"firstName":"Yunus Emre","lastName":"Çiçek","age":20}'


convert = json.loads(data)

print(convert)
print(type(convert))

student = {
    "firstName":"Enes Emir",
    "lastName":"Çiçek",
    "age":17
}

convertJson = json.dumps(student)

print(convertJson)
print(type(convertJson))


with open("students.json","w",encoding="utf-8") as f:
    json.dump(student,f)














