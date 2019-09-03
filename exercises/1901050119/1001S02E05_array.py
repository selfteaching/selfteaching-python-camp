a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#reverse
a_list.sort(reverse = True)

i = 0
while(i < len(a_list)):
    a_list[i] = str(a_list[i])
    i = i + 1

s = ''
a_str = s.join(a_list)
b_str = a_str[2:8]

b_list = []
s_len = len(b_str)

for i in range(s_len):
    b_list.append(b_str[s_len-1-i])
   
print(b_list)

s1 = ''
c_str = s.join(b_list)
print(c_str)

num = int(c_str)

print(bin(num))
print(oct(num))
print(hex(num))
