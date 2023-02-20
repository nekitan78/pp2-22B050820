
def even(n):
    for x in range(n + 1):
        if x%2 == 0:
          yield x
          



n = int(input())

nums = even(n)
for x in nums:
    print(x)