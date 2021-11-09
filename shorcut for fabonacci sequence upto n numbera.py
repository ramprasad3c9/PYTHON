#short cut for fabonacci sequence upto n numbers
n=int(input("enter the number:"))
a=0
b=1
while n>0:
    print(a,end=",")
    a,b=b,a+b
    n-=1
