array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
array.reverse()
print(array)

str1=''.join('%s'%id for id in array)
print(str1)

str2=str1[2:8]
print(str2)

str3=str2[::-1]
print(str3)

int1=int(str3)
print(int1)

int2="{0:b}".format(int1)
print(int2)

int3="{0:o}".format(int1)
print(int3)

int4="{0:x}".format(int1)
print(int4)
