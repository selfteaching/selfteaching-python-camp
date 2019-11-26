list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.reverse()                         #reverse the list
str1 = ""
for i in list1:
    str1 = str1 + str(i)                #append the string
#print (str1)
str1 = str1[2:8]                        #slice the string 
#print(str1)

list1 = list(str1)                      #reverse the string by" for cycle"
list1.reverse()
str1 = ""
for i in list1:
    str1 = str1 + str(i)
int1 = int(str1)
#print(int1)
print(bin(int1))                        #output the bin&oct&hex numbers
print(oct(int1))
print(hex(int1))
'''
str2 = ""
for i in str1:
    str2[-1] = i
print(str2)
'''