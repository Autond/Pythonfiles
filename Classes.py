class Calculator:
    num=100 # class variables

    def __init__(self):
        print("I am a constructor and called automatically when object is created")
    def getData(self): # function inside the class is called methods
        print("I am now executing  as method in class")

obj=Calculator() #syntax for creating object of a class to call the variables and methods inside tha class
#print(obj.num)
#obj.getData()

class Calculator1:
    num1=100 # class variables

    def __init__(self,a,b):
        self.FirstNumber = a # instance variables change everytime an object is called and whatever value it passes is stored here
        self.LastNumber = b
        print("I am called automatically when object is created")
    def getData1(self): # function inside the class is called methods
        print("I am now executing  as method in class")

    def summation(self):
        return self.FirstNumber+self.LastNumber


obj=Calculator1(2,3) #
print(obj.num1)
obj.getData1()