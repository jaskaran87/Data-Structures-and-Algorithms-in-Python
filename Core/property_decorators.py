class Employer:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @property
    def email(self):
        return ('{first}.{last}@email.com'.format(first = self.first,last = self.last))

    @property
    def fullname(self):
        return ('{first} {last}'.format(last = self.last, first = self.first))

    @fullname.setter
    def fullname(self, name):
        self.first, self.last = name.split(' ')


    @fullname.deleter
    def fullname(self):
        print('Delete fullname')
        self.first = None
        self.last = None


emp_1 = Employer('jaskaran', 'singh')
print("Frist Name: {first} ".format(first = emp_1.first))
print("last Name: {last}".format(last = emp_1.last))
print(emp_1.email)

emp_1.fullname = 'Amandeep singh'

print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)
