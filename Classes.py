class Calculator:
    num=100 # class variables

    def __init__(self):
        print("I am a constructor and called automatically when object is created")
    def getData(self): # function inside the class is called methods
        print("I am now executing  as method in class")

obj=Calculator() #syntax for creating object of a class to call the variables and methods inside tha class
#print(obj.num)
#obj.getData()



