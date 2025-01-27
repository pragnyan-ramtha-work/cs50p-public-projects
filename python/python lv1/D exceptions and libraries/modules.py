import random
#when func is imported put func.(the func) to work ex. from random import choice
result = random.choice(["boy","girl"])
print(result)
result1 = random.randint(1,10)
#produces random numbers
roll = [1,2,3,4,7,9]
result2 = random.shuffle(roll)
for i in roll:
    print(i)
