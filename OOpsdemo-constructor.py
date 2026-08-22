# self keyword is mandatory for calling variable names into method
# instance and class variable have whole different purpose (one is attached to object and other is not)
# constructor name should be __init__
# new keyword  is not required to create object

class Calculator1:
    num1=100 # class variables

    def __init__(self,a,b):
        self.FirstNumber = a # instance variables change everytime an object is called and whatever value it passes is stored here
        self.LastNumber = b
        print("I am called automatically when object is created")
    def getData1(self): # function inside the class is called methods
        print("I am now executing  as method in class")

    def summation(self):
        return self.FirstNumber+self.LastNumber+Calculator1.num1
    #instance variable always called as self.variablename
    #class variable always called as class.variablename or self.classvariablename


obj=Calculator1(2,3) #creation of object
print(obj.num1)
obj.getData1()
print(obj.summation())