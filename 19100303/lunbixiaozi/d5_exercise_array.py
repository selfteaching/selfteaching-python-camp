shuzu = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuzu.reverse()
print (shuzu)
zifuchuan = ''
for i in range(len(shuzu)):
    zifuchuan = zifuchuan + str(shuzu[i])

print(zifuchuan)

zifuchuan_3t8= zifuchuan[3:9]
print(zifuchuan_3t8)
list_3t8 = []
for i in range(len(zifuchuan_3t8)):
    list_3t8.append(zifuchuan_3t8[i])
list_3t8.reverse()
print (list_3t8)

string_3t8=''
for i in range(len(list_3t8)):
    string_3t8 = string_3t8 + str(list_3t8[i])

int_3t8 = int(string_3t8)
int_3t8_bin = bin(int_3t8)
int_3t8_oct = oct(int_3t8)
int_3t8_hex = hex(int_3t8)

print('bin: ' + str(int_3t8_bin))
print('oct: ' + str(int_3t8_oct))
print('hex: ' + str(int_3t8_hex))
