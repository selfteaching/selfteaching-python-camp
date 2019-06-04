list1 = []
for x in range(10):
    list1.append(x)
print(list(list1))
list1.reverse()
print(list(list1))

list2= [str(list_str) for list_str in list1]     
str1 = "".join(list2)                     

substring =str1[2:8]


substring = substring[::-1]

subint = int(substring)

bin_result = bin(subint)
oct_result = oct(subint)
hex_result = hex(subint)

print(bin_result, oct_result, hex_result, sep="\n")