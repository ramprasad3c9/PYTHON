#provide user with three options using funtions
print("pick one of the following three options")
print("1.find  if a number is even or odd number")
print("2.print all the even number in a given range")
print("3.print all the odd number in a given number")
def even_odd(n):
        if n%2==0:
            return True
        else:
            return False
opt=int(input("select the option:"))
if opt==1:
    n=int(input("enter a number:"))
    if even_odd(n)==True:
        print(n,"is a even number")
    else:
        print(n,"is a odd number")
elif opt==2:
    a,b=map(int,input("enter two numbers:").split())
    for i in range(a,b+1):
        if even_odd(i)==True:
            print(i,end=",")
else:
    a,b=map(int,input("enter two number:").split())
    for j in range(a,b+1):
        if even_odd(j)==False:
            print(j,end=",")
