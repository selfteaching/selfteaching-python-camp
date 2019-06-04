array=[0,1,2,3,4,5,6,7,8,9]

array.reverse()

print(array)



s = ''

for i in range(0,10):  

    array[i]=str(array[i])

string=s.join(array)

print(string)

target=string[2:8]

print(target)

integer=int(target[::-1]) 

print(integer)

print(bin(integer),oct(integer),hex(integer))