array=[0,1,2,3,4,5,6,7,8,9]
array.reverse()
print(array)
str1=[]
for i in range(len(array)):
    str1.append(str(array[i]))
print(str1)
string=str1[0]
for i in range(1,len(str1)):
    string+=str1[i]
#print(string)
str2=string[2:8]
print(str2)
str2=str2[::-1]
print(str2)
#print(int(str2,10))
a=int(str2,10)
#print(a)
print("{0:b}".format(a))
print("{0:o}".format(a))
print("{0:X}".format(a))
