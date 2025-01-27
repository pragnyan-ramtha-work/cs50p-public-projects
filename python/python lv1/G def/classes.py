class family:
   
 def __init__(self,name,height,age):
        if not name:
            raise ValueError("whers the name bro")
    
        self.name = name
        self.age = age
        self.height = height  #given that the value of height is 
        def age(self):
             return self._age
        def age(self,age):
             if age < 18:
                  raise ValueError("minor")
        self._age =age 


 def __str__(self):
        return f"{self.name} is {self.age} old"
 
def main():
    member = get_info()
    family.age = "hi wtf"
    print(member)




def get_info():
    name = input("name: ")
    age = int(input("age: "))
    height = int(input("height: "))
    return family(name,age,height)






   







    





 
# print(f"{member.name} is {member.height} long and {member.age} old")


main()  
   
