import re

txt = "aaadsabbbbcbbbb"

x = re.search('a(b*)b', txt)

print(x)