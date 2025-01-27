import time 
import random as ra

le = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
sy = ["!","@",'#',"$","%","^","&","*","(",")","-","_","+","=","[","]","{","}",":",";","<",">","?",".",",","|"]
ke = le + sy


word = input("encryption: ")
urword = list(word)
z = len(urword)



for i in range(0,10):
    for i in range(0,z):
        print(ra.choice(ke),end="")
    time.sleep(0.1)
    print()

h1 = []

for i in range(z):
    h1.append(word[i])

    for i in range(z):
        h1.append(ra.choice(ke))
        print(h1[i],end="")
    print()


    for i in range(z):
        h1.pop()
    time.sleep(0.1)    




time.sleep(10)