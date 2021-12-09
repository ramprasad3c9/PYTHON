#spy number
#a number n is called a spy number
#if sum of digits of that number s is equal to product of digis of that number p
n=int(input("enter a number:"))
s=0
p=1
q=n
a=n
while n:
    r=n%10
    s+=r
    n=n//10
while q:
    r=q%10
    p*=r
    q=q//10
if s==p:
    print(a,"is a spy number")
else:
    print(a,"is not a spy number")
