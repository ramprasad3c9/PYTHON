#patterns using for loops
n=int(input('enter a number:'))
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print(1,end=' ')
        else:
            print(0,end=' ')
    print()
