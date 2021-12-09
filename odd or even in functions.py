#write a funtion to find the whether the given number is even or odd
#ex:12-->even
#ex:15-->odd
def even_odd(a):
    if a%2==0:
        print(a,"is a even number")
    else:
        print(a,"is a odd number")
a=int(input("enter a number:"))
even_odd(a)
