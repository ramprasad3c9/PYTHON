#finding the n is perfect number or not
n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(n,"is a perfect number")
else:
    print(n,"is a not a perfect number")
