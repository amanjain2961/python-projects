tax =0
pr=int(input("enter the price of bike"))
if pr>100000:
    tax =15/100*pr
    print("tax to be paid",tax)
elif pr >50000 and pr <=100000:
    tax =10/100*pr
    print("tax to be paid",tax)
else:
    tax=5/100*pr 
    print("Tax to be paid ",tax)