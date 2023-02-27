import re

txt = "aaadsabbbbcbbbb"

x = re.search('a.*b', txt)

print(x)