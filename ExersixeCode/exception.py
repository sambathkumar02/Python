a=10
b=0
try:
    print(a/b)
except ZeroDivisionError as e:
    print('you got an eror',e)
finally:
    print('bye')