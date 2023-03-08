a = [1, 2, 3, 4, 5, 6]

with open("output.txt", "w") as f:
    for i in a:
        f.write(str(i))