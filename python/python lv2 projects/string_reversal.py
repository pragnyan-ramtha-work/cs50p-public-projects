q =  input("string: ").lower()

e = list(q)


for i in range(len(q)):
    print(e[len(q) - i -1],end="")
