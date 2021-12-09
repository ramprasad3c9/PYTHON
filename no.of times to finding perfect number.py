#fining no.of times to finding the perfect number
t=int(input("enter a t value:"))
for number in range(t):
    n=int(input("enter a number:"))
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        print(n,"is a perfect number")
    else:
        print(n,"is not a perfect number")
