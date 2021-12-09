#print all the factors of a given number n using for loop
n=int(input())
for i in range(1,n//2+1):
    if n%i==0:
        print(i)
print(n)
