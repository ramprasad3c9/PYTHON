#write a python program to find whether the given number is palindrome or notusing functions
def reverse(n):
    rev=0
    while(n):
        r=n%10
        rev=rev*10+r
        n=n//10
    return rev
def palindrome_not(n):
    if reverse(n)==n:
        return True
    else:
        return False
n=int(input("enter a number:"))
if palindrome_not(n)==True:
    print(n,"is a palindrome")
else:
    print(n,"is not a palindrome")
