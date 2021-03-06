'''
Method resolution order in Python Inheritance
Method Resolution Order :
Method Resolution Order(MRO) it denotes the way a programming 
language resolves a method or attribute. 

Python supports classes inheriting from other classes. 

The class being inherited is called the Parent or Superclass, 
while the class that inherits is called the Child or Subclass. 

In python, method resolution order defines the order in which 
the base classes are searched when executing a method. 

First, the method or attribute is searched within a class and 
then it follows the order we specified while inheriting. 

This order is also called Linearization of a class and set of 
rules are called MRO(Method Resolution Order). 

While inheriting from another class, the interpreter needs 
a way to resolve the  methods that are being called via 
an instance. 

Thus we need  the method resolution order. For Example
'''
class A(object):
    pass

print('Class A MRO: ')
print(A.__mro__)
print('-------------------------')
'''
Class A MRO: 
(<class '__main__.A'>, <class 'object'>)
'''

class B(A):
    pass

print('Class B MRO:')
print(B.__mro__)
print('-------------------------')

'''
-------------------------
Class B MRO:
(<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
-------------------------
'''

class C(A):
    pass

print('Class C MRO:')
print(C.__mro__)
print('-------------------------')
'''
Class C MRO:
(<class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
-------------------------
'''

class D(B):
    pass

print('Class D MRO:')
print(D.__mro__)
print('-------------------------')
'''
Class D MRO:
(<class '__main__.D'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
-------------------------
'''

class E(B, A):
    pass

print('Class E MRO:')
print(E.__mro__)
print('-------------------------')
'''
Class E MRO:
(<class '__main__.E'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
'''

class F(object):
    pass

class G(object):
    pass

class H(F,G,A):
    pass

print('Class H MRO:')
print(H.__mro__)
print('-------------------------')

'''
Class H MRO:
(<class '__main__.H'>, <class '__main__.F'>, <class '__main__.G'>, <class '__main__.A'>, <class 'object'>)
'''

class I(H):
    pass
print('Class I MRO:')
print(I.__mro__)
print('-------------------------')

'''
Class I MRO:
(<class '__main__.I'>, <class '__main__.H'>, <class '__main__.F'>, <class '__main__.G'>, <class '__main__.A'>, <class 'object'>)
'''

class J(H):
    pass
print('Class J MRO:')
print(J.__mro__)
print('-------------------------')

'''
Class J MRO:
(<class '__main__.J'>, <class '__main__.H'>, <class '__main__.F'>, <class '__main__.G'>, <class '__main__.A'>, <class 'object'>)
'''

class K(B):
    pass
print('Class K MRO:')
print(K.__mro__)
print('-------------------------')

'''
Class K MRO:
(<class '__main__.K'>, <class '__main__.B'>, <class '__main__.A'>, <class 'object'>)
'''

 # Note no Error in this case
class L(B,A):
    pass
print('Class L MRO:')
print(L.__mro__)
print('-------------------------')

'''
Class L MRO:
(<class '__main__.L'>, <class '__main__.B'>, <class '__main__.A'>, <type 'object'>)
'''

# NOTE Error B has inherit A Class already If we inherit A, B then it will produce error TypeError 
class N(A, B):
    pass

# Traceback (most recent call last):
#   File "/var/www/html/Python-Core/MRO.py", line 107, in <module>
#     class L(A,B):
# TypeError: Cannot create a consistent method resolution
# order (MRO) for bases A, B
