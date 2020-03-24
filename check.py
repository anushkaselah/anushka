x=int(input("add number:"))
if x>1:
  for i in range(2,x//2):
     if(x%i)==0:
      print(x,"not prime")
      break
  else:
      print(x,"prime")
else:
    print(x,"not prime")