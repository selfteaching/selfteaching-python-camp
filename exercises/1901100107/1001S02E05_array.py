#1.creat a file named '1001S02E05_array.py'
list1=[1,2,3,4,5,6,7,8,9]

#2.reverse the list
list1.reverse()
print(list1)  

#3.convert list to strings
list_str1 = [ str(i) for i in list1 ]
str1 = "".join(list_str1) 
print(str1)

print(str1[2:8]) #4.slicing the 3rd-8th characters, both inclusive

#5.Reverse String
list2=list(str1) 
list3=[int(i) for i in list2] 
list3.reverse() 
list_str2 = [str(i) for i in list3] 
str2 = "".join(list_str2) 
print(str2)

#6.convert result_str to integer
int1=int(str2)  
print(int1)
print('str2',str2,type(str2),type(int1)) #check int1 format 

#7. Convert int1 to binary, octal & hex
bin1=bin(int1)
oct1=oct(int1)
hex1=hex(int1)

#8. print 
print(bin1,'\t',oct1,'\t',hex1)









