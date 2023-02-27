import re
text = "PythonEdition"
print(re.findall('[A-Z][^A-Z]*', text))
