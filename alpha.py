Dict_input={"student1":"Aman","student2":"Dheeraj","student3":"Mohit","student4":"Kanika","student5":"Amrita"}
print("The original list is:"+ str(Dict_input))
print(sorted(Dict_input.items(),key=lambda kv:kv[1]))