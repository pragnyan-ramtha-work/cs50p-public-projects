#to associate one value with another
family = {"pik":"M",
          "bhav":"F",
          "dad":"M"
           }

print(family["pik"])
print(family["bhav"])
for member in family:
    print(member,family[member],sep=", ")
#for multiple values do [of{}] i.e lists of dict
family2 = 23
for i in range(3):
    print("#")