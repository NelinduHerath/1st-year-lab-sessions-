num_units= int(input("enter num_units -"))
if num_units <= 50:
    bill= num_units*50
elif num_units<=100:
      bill= 50*50+(num_units-50)*100
else:
    bill=(50*50)+(50*100)+(num_units-100)*150
bill=bill+100
print("bill is",bill)
