#using range()
#read two numbers from user(in single line) and print all the even numbers in that range
a,b=map(int,input().split())
for i in range(a,b,2):
    print(i)
