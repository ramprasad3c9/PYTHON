#print sum of a given number
n=int(input("enter a number:"))
s=0
while n:
    r=n%10
    s+=r
    n=n//10
print(s)
