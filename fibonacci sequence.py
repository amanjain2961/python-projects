num1=0
num2=1
print("fibonacci sequence")
for i in range(int(input("enter the range"))):
    print( num1 , end='  ')
    res = num1 +num2
    num1=num2 
    num2= res