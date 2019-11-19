class MyClass(object):
 	pass

print(dir())

x = MyClass()

print(MyClass)

print (x)

print(type(x))

print (MyClass == type(x))
# ------------------------------------------
class MyClassT(object):
	def __init__(self):
		self.x = 5

def printHam(self):
	print('here')

def a(self,a):
	print(a)

#1 Parameter: class Name
#2 Parameter: baseClass
#3 parameter : argumet , fun, parameter
# type is main meta class 

TypeClass = type('TypeClass', () , {"x": 5 , 
	"printHam": printHam,
	"aFun": a
	})

m = MyClassT()
t = TypeClass()
print(m.x)
print(t.x)
t.printHam()
t.aFun(78)

'''
Metaclass: A class that allow the creation of other classes
python uses 'type' by default

print( "1".__class__) # str
print( "1".__class__.__class__) # type
print(type(type("1"))) # type
print(type("1")) # str
'''