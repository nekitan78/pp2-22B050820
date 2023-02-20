def square(n):
    for i in range(1, n + 1):
        yield (i * i)

n = int(input())

nums = square(n)

for x in nums:
    print(x)
