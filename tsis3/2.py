
x = lambda a: a + 1
print(x(4))


y = lambda a, b: a * b 
print(y(5, 3))

def myFun(x, b):
    return lambda a: a * x * b

print(myFun(3,4)(2))