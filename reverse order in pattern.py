#take n from user and print the following pattern
n=int(input())
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(i, end=" ")
    print()
