n = int(input())
i=1
while i<=n:
    space=1
    while space<=n-i:
        print(' ',end= "")
        space= space+1
    num = 1
    while num <=i:
        print(num,end="")
        num=num+1
    print()
    i=i+1
