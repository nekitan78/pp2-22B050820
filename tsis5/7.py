def div(n):
    for x in range(1, n + 1):
        if x % 3 == 0 or x % 4 == 0:
            yield x

n = int(input())

nums = div(n)

for x in nums:
    print(x)