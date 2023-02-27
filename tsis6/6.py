import re

txt = "aaa dsab,bbbcb.bbb"

x = re.sub( "[ ,.]" ,":", txt)

print(x)