a=int(input("Enter number1:"))
b=int(input("Enter number2:"))
if a<b:
    r=a
else:
    r=b
for i in range(1,r+1):
    if a%1==b%1==0:
        print(i)    
