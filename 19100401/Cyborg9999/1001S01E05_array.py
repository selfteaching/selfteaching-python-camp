array=[0,1,2,3,4,5,6,7,8,9]
array.reverse()
#print(array)

zfc=str(array[0])
for i in range(1,10):
    zfc=zfc+str(array[i])
#print(zfc)

part=zfc[2:8]
#print(part)

part2=int(part[::-1])
#print(part2)

print(bin(part2),oct(part2),hex(part2))



