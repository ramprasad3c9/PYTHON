#electricity bill:
ID=int(input("enter a customer ID:"))
units=int(input("enter electricity bill:"))
if 199>=units:
    bill=units*1.20
elif 200<=units and units<400:
    bill=units*1.50
elif 400<=units and units<600:
    bill=units*1.80
else:
    bill=units*2.00
if bill>400:
    SC=bill*0.15
elif bill<=400:
    SC=0.0
total=bill+SC
print("Customer ID:",ID)
print("Units Consumed:",units)
print("Amount Charges:",bill)
print("Surcharge Amount:",SC)
print("Net Amount Paid By The Customer:",total)

