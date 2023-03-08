import os


def sm(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

print(sm("output.txt"))