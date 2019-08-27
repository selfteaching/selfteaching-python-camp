array=[0,1,2,3,4,5,6,7,8,9]
array.reverse()

array1 = [str(i) for i in array]
print(array1)
array2 = ''.join(array1)
print(array2)

array3 = array2[2:8]

array4= []
for i in array3:
    array4.append(str(i))
array4.reverse()
array5=''.join(array4)
array6=[]
for i in array5:
    array6.append(int(i))
print(array6)

array7=[]
array8=[]
array9=[]
for i in array6:
    array7.append(bin(i))
    array8.append(oct(i))
    array9.append(hex(i))
print(array7, array8, array9)
