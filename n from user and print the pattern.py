#take n from user and print the following pattern
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j, end=" ")
    print()
