#proper factor
n=int(input())
s=0
for i in range(1,n):
    if n%i==0:
        s+=i
if s==n:
    print(n,"is a proper factor")
else:
    print(n,"is a not a proper factor")
