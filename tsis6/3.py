import re

txt = "l_lllld_"

x = re.search('[a-z]_', txt)

print(x)