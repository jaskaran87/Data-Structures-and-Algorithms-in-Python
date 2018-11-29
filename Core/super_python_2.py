class Thrid(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('Thrid object')

    def printA(self):
        print (self.a)
        print(self.b)

class First(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('First object')        

    def printA(self):
        print (self.a)
        print(self.b)

class second(First, Thrid):
    def __init__(self, a, b):
        print('with supper key word python2')
        super(second,self).__init__(21,41)
        super(second,self).printA()

        print('With class name')
        # with class Name
        First.__init__(self,a,b)
        First.printA(self)
        Thrid.__init__(self, 3,5)
        Thrid.printA(self)

obj = second(50,20)