#take n from user and print the following pattern
n=int(input())
k=2
for i in range(1,n+1):
    for j in range(1,n+1):
        print(k, end=" ")
        k+=2
    print()
