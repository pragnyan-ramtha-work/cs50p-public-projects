names = []

with open("name2.txt") as file:
    for name in sorted(file):
        print('hello',name)

#sorted() sorts names over the a-z
