#In Python, the term monkey patch only refers to dynamic modifications of a class or module at run-time.

import monkey_patching_class

def monkey_function(self):
	print('Monkey Function')


monkey_patching_class.MonkeyClass.fun = monkey_function

obj = monkey_patching_class.MonkeyClass()

obj.fun()

#As we can see, we did make some changes in the behavior of fun() in MonkeyClass using the function we defined, monkey_function(), outside of the module monkey_patching_class.