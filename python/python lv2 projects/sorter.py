import random as ra

num =  [0,1,2,3,4,5,6,7,8,9]

rb =  input("number?" )

new = list(rb)

#for i in range(0,ra.choice(num)):
    #x = ra.choice(num)
    #new.append(x)

k = len(new)


for i in range(0,k):
    print(new[i],end="")
print() 



new1 = sorted(new)



for i in range(0,k):
    print(new1[i],end="")
print() 
