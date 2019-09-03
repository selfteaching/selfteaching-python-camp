a_list=[0,1,2,3,4,5,6,7,8,9]
a_list.reverse()
a_list=a_list[2:8]
a_list.reverse()
print(a_list)
for bin_element in a_list:
     print (bin_element, bin(bin_element))
for oct_element in a_list:
     print (oct_element, oct(oct_element))
for hex_element in a_list:
     print (hex_element, hex(hex_element)) 