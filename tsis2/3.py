list1 = ["orange", "bull", "apple"]
list2 = [1, 2, 3, 4, 5, 6]
for x in list1:
    if x == "bull":
        continue
    for y in list2:
        if y == 5:
            continue
        print(x,y)