#super key word in python 3
class FirstClass:
    def __init__(self, a, b):
        print('Frist class __init__')
        self.a = a
        self.b = b
        
    def printA(self):
        print('FirstClass PrintA function')

class sClass:
    def __init__(self, a, b):
        print('Frist class __init__')
        self.a = a
        self.b = b
        
    def printA(self):
        print('sClass PrintA function')

class NextClass(FirstClass, sClass):
    def __init__(self, a, b):
        super().__init__( a, b)
        super().printA()
        sClass.printA(self)

a = NextClass(50,42)

