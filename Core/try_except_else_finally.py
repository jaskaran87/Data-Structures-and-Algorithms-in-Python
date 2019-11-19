def divide(x, y):
  try:
    result = x / y
  except ZeroDivisionError:
    print("division by zero!")
  else:
    print("result is", result)
  finally:
    print("executing finally clause")

divide(20, 10) # else part and finally clause will excute

divide(20, 0) # except part and finally clause will excute

divide('s', 0) # finally clause will excute after that show Error TypeError

