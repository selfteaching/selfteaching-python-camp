num_list=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
num_list.reverse()
num_str=[str(i) for i in num_list]
x="".join(num_str)
n=list(x[2:8])
n.reverse()
str1="".join(n)
num1=int(str1)
print(bin(num1))
print(oct(num1))
print(hex(num1))