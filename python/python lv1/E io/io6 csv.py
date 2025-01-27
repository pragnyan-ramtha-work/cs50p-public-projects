import csv

name = input("")
gender = input("")

with open("su.csv") as file:
    writer = csv.DictWriter(file, feildnames=["name","gender"])
    writer.writerow({"name":name,"gender":gender})