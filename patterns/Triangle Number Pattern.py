rows = int(input())
for i in range(0,rows+1):
    # nested loop
    for j in range(0,i):
        # display number
        print(i, end='')
    # new line after each row
    print('')
