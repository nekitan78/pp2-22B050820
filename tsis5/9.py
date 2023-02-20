def down(n):
    for x in range(0, n + 1):
        yield 10 - x

n = 10

nums = down(n)

for x in nums:
    print(x)