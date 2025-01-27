names = []

for _ in range(3):
    names.append(input("gimme name "))
    # append saves input names in list

for name in sorted(names):
    print("hello",name)