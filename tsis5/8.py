
def squares(a, b):
    for x in range(a, b + 1):
        yield x * x





a = 10
b = 15

nums = squares(a , b)
for x in nums:
    print(x)
