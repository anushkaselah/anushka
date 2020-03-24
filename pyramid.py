n=int(input("enter no of rows:"))
k=2*n-2
for i in range(0,n):
    for j in range(1,k):
        print(end=" ")
    k=k-1
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")            
