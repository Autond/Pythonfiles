
from Classes import Calculator
class ChildImpl(Calculator):
    num2=100

    def __init__(self):
        Calculator.__init__(self)  # this is how you call parent constructore by creating a child constructor


    def getCompleteData(self):
        return self.num+ self.num2

obj= ChildImpl()
print(obj.getCompleteData())