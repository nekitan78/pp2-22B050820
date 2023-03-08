import os

ch = os.access('c:\pp2 spring\\tsis7\\input.txt', os.F_OK)

if ch:
    os.remove(".\input.txt")