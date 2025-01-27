name = input("say somthing ")

with open("name2.txt","a") as file:
    file.write(f"{name}\n")
    #better than i02 since auto save