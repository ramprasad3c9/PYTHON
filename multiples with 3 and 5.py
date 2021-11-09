#printing all multiples with 3 and 5
a=int(input("enter a number:"))
b=int(input("enter a number:"))
while a<=b:
    if a%3==0 or a%5==0:
        print(a,end=',')
    a+=1
