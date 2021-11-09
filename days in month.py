#days in month:
M=int(input("enter a month number:"))
if M==1 or M==3 or M==5 or M==7 or M==8 or M==10 or M==12:
    print("month",M,"has 31 days")
elif M==2:
    print("month",M,"has 28 days")
elif M==4 or M==6 or M==9 or M==11:
    print("month",M,"has 30 days")
