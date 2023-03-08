a = "affdJGFhggdhGhd"

def cnt(x):
    for a in x:
       c = sum(1 for i in x if i.isupper())
       s = sum(1 for i in x if i.lower())
    print(c, s)

cnt(a)