import csv

students = []



with open("su.csv") as file:
    for line in file:
        name,gender = line.rstrip().split(",")
        student = {"name":name,"gender":gender}
        students.append(student)




for student in sorted(students):
    print(student[name],"is a",student[gender])