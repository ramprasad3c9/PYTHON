#another way of writing while loop without multiples of 3:
n=int(input("enter a number:"))
i=1
while i<n:
    if i%3==0:
        i+=1
        continue
    print(i,end=',')
    i+=1
