
class Pen:
    def __init__(self,name:str,color:str,length:str) -> None:
        self.name = name
        self.color = color
        self.length = length
        self.fcap_on = True

    def cap_on(self) -> None:
        if  self.fcap_on:
            print(f"the {self.name} pen is capped on shut")
        else:
            self.fcap_on = True
            print(f"the {self.name} pen was capped on")    

    def cap_off(self) -> None:
        if  self.fcap_on:
             self.fcap_on= False
             print(f"the {self.name} pen's cap was removed ") 
        else:
            print(f"the {self.name} pen is already removed")
           
    def write(self,time:int):
        if self.cap_off:
            print(f"starting to write for {time} seconds")
        else:
            print("remove the cap first baka")

    def __add__(self,other):
       return f"{self.name}+{other.name}"
    
    def __mul__(self,other):
        return f"{self.name}+{other.name}"
    
    def __str__(self) -> str:
        return f"{self.name,self.color}"
    
    def __repr__(self) -> str:
        return f"{self.name},{self.color},{self.length}"
    
    def __str__(self) -> str:
        return f"{self.name} is {self.color} color {self.length} long "
    
def main():
    newpen = getpen()
    print(newpen)



def getpen():
    name =input("name; ")
    length = input("length; ")
    color = input("color; ")
    return Pen(name,color,length)

main()


