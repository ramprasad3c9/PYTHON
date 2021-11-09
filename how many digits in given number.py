#print the how many digits in given number
n=int(input("entera number:"))
l=0
while n:
    r=n%10
    l+=1
    n=n//10
print(l)
