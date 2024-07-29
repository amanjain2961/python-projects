n=int(input("enter the number  for the reverse pattern :"))
k = n
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=' ')
    print()