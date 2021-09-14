import random

# result = dir(random)


result = random.random()
result = random.random() * 100
result = int(random.uniform(10,100))
result = random.randint(1,100)

names = ["Yunus","Enes","Furkan","Ali"]
greeting = "Hello there"

# result = names[random.randint(0,len(names)-1)]
result = random.choice(names)
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste)
result = liste

liste = range(100)
result = random.sample(liste,3)
result = random.sample(greeting,2)

print(result)


