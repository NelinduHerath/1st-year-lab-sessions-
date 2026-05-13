units =int(input("enter number of units"))
if units <= 30:
    bill =(units*5)+500
elif units<=60:
    bill =(30*5)+((units-30)*10)+500
elif units<=100:
    bill=(30*5)+(30*10)+((units-60)*15)+500
else:
    bill(30*5)+(30*10)+(40*15)+((units-100)*50)+500
print("total bill is",bill)

        
        
