#write a function which takes two numbers and prints the largest of those:
#ex:12,18
#18 is a largest number
def number(a,b):
    if a>b:
        print(a,"is a largest number")
    else:
        print(b,"is a largest number")
a,b=map(str,input().split())
number(a,b)
