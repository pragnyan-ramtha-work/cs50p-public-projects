class Pen:
    def __init__(self,name,length) -> None:
        self.name = name
        self.length = length

def main():
    pen = getpen()
    print(f"{pen.name} is {pen.length} cm long")




    @property
def getpen():
    name = input("name; ")        
    length = input("length; ")
    return Pen(name,length)

main()