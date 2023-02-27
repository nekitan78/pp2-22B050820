import re

txt = "LlDssSf"

x = re.search('[A-Z][a-z]', txt)

print(x)