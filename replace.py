test_list=[1,2,3,4,3,4,8,10,2,3]
print("The original list is:"+ str(test_list))
N='rep'
has=set()
for i in range(len(test_list)):
    if test_list[i] in has:
         test_list[i]=N
    has.add(test_list[i])                   
print("The duplication alteret list:"+ str(test_list))
