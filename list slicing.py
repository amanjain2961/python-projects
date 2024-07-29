n =int(input("enter number of elements"))
a=[]
for i in range(n):
    x=int(input())
    a.append(x)
print(a) 
for i in a[0::2]:
    print(i)


