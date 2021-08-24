website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"


message = " Hello World "
message = message.strip()
#print(message)

#website = website.replace("http://www.","").replace(".com","")
#print(website)

# course = course.lower()
#print(course)

# print(website.count("a"))

isSuccess = website.startswith("http")
# print(isSuccess)
isSuccess = website.endswith(".com")
# print(isSuccess)

isExist = website.find(".com")
# print(isExist)



#course = course.isalpha()
# print(course)

message = "Contents"
message = message.center(50,"*")
print(message)

#course = course.replace(" ","-")
print(course)

message = "Hello World"
message = message.replace("World","There")
print(message)

course = course.split()
print(course)

