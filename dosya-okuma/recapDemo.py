

students = ["Yunus Emre","Enes Emir","Furkan","Melikber"]

file = open("students.txt","a")

for x in students:
    file.write(f"{x}\n")

file.close()