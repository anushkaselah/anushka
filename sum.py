test_list=[(4,5),(6,1),(3,6),(4,3),(2,5)]
print("The tuple list is:"+ str(test_list))
k=7
res=[]
for ele in test_list:
    if ele[0]+ele[1]==k:
       res.append(ele)
print("List after checking:"+str(res))    
