#patterns using for loops
n=int(input('enter a number:'))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
