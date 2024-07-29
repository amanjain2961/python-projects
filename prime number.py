start = int(input("enter the number from where to start "))
end = int(input("enter the number where you have to stop"))
print("Prime numbers between", start, "and", end, "are:")

for num in range(start, end + 1):
    
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)