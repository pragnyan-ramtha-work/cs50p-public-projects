x = int(input("base length of pyramid is? "))

for i in range (1,x):
    print(f"{(x-i)* " "}{(2*i -1) * "#"}")