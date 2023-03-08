a = "abcba"

b = ''.join(reversed(a))

c = True

for i in range(len(a)):
    if a[i] == b[i]:
        c = True
    else: 
        c = False
        break

print(c) 


        
        