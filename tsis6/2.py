import re

txt = "aaadsabbcbbbb"

x = re.search('ab?bb', txt)

print(x)