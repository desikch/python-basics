num=input()
x=[int(i) for i in num]
e=0
o=0
for i in range(0,len(x)):
    if x[i]%2==0:
        e=e+x[i]
    else:
        o=o+x[i]
print(e,o)
