message = "Hello there, My name is Yunus Emre"

print(message)


# print(message.upper())             # All letter are big
# print(message.lower())             # All letter are written small
# print(message.title())             # First letter of all words are written big
# print(message.capitalize())        # First letter of only the first word are written big
# print(message.strip())             # If there is any blank in the beginning of the string, it will be destroyed by this code
# print(message.split()) 

"""
message = message.split()
message = "**".join(message)
print(message)

"""
"""
index = message.find("Emre")
print(index)

"""

# isFound = message.startswith("H")
# isFound = message.endswith("e")
# print(isFound)

# message = message.replace("e","a")
# print(message)

message = message.center(50,"*")
print(message)





