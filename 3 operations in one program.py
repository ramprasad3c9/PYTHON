#provide user with three options
#1.find if a number is even or odd
#2.print all the even number in a given range
#3.print all the odd numbers in a given range
#if user choose option-1, then ask him for a number to find if the number is even or odd
#if user choose option-2, then ask him range(a,b) to print all the even number in the range
#if user choose option-2, then ask him range(a,b) to print all the odd number in the range

print("pick one of the following three options")
print("1.find  if a number is even or odd number")
print("2.print all the even number in a given range")
print("3.print all the odd number in a given number")
opt=int(input("select the option:"))
if opt==1:
    n=int(input("enter a number:"))
    if n%2==0:
        print(n,"is a even number")
    else:
        print(n,"is odd number")
elif opt==2:
    a,b=map(int,input('enter a two number:').split())
    for i in range(a,b+1):
        if i%2==0:
            print(i,end=",")
else:
    a,b=map(int,input("enter two numbers:").split())
    for i in range(a,b+1):
        if i%2!=0:
            print(i,end=",")
