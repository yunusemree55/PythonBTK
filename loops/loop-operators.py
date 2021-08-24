

# for item in range(1,100,2):
#     print(item)


# print(list(range(1,100,2)))


index = 0
greeting = "Hello there"

# for index,letter in enumerate(greeting):
#     # print(letter)
#     print(f"index: {index} letter: {letter}")
    

list1 = [1,2,3,4,5]
list2 = ["a","b","c","d","e"]
list3 = [100,200,300,400,500]

print(list(zip(list1,list2,list3)))

# for item in zip(list1,list2,list3):
#     print(item)

for a,b,c in zip(list1,list2,list3):
    print(a,b,c)



