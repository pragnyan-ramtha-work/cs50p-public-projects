def div_check(x):
    if x % 15 == 0:
        y = 1
    elif x % 3 == 0:
        y = 2
    elif x % 5 == 0:
        y = 3
    else:
        y = 0
    return y        


for i in range(1,101):
   y = div_check(i)
   if y == 0:
       print(i,end=" ")
   elif y == 2:
    print("fizz",end=" ")
   elif y == 3:
       print("buzz",end=" ")
   else:
       print("fizz buzz",end=" ")    
               
