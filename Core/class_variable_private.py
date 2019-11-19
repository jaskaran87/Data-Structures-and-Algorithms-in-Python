class Test:
  def  __init__(self, host, user, password):
  	self.host = host
  	self._user = user #protected
  	self.__password = password #private

t = Test('localhost', 'jaskaran', 'password')

#asscess private variable

print(t._Test__password)
