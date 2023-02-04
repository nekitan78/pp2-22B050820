myTuple = ("apple", "banan", "orange")
for x in myTuple:
    print(x)
myTuple *= 2
print(myTuple)

myTuple = list(myTuple)
myTuple.append("watermelon")
myTuple = tuple(myTuple)
print(myTuple)