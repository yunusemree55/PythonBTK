import re


# re module
# regular expression

str = "Türkiye Cumhuriyeti"

# re.findall()

result = re.findall("Türkiye",str)


# re.split()

result = re.split("i",str)

# re.sub()

result = re.sub(" ","*",str)


# re.search()

result = re.search("Cumhuriyet",str)

# result = result.span()
 
result = re.findall("[i]",str)
result = re.findall("[i-ü]",str)

result = re.findall("...",str)
result = re.findall("^T",str)
result = re.findall("e$",str)
result = re.findall("Tür*kiye",str)
result = re.findall("Cumhu+riyeti",str)

print(result)

