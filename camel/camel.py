c_c = input("camelCase: ").strip()

for l in c_c:
    if l.islower():
        print(l, end="")
    else:
        print("_" + l.lower(), end="")

print()
