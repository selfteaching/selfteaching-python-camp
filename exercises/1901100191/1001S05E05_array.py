a_list=[0,1,2,3,4,5,6,7,8,9]
a_list.sort(reverse=True)
print(a_list)
b=''.join(str(i) for i in a_list)
print(b)
c=b[2:8]
print(c)
d=c[::-1]
print(d)
int_value=int(d)
print(int_value)
print(bin(int_value))
print(oct(int_value))
print(hex(int_value))