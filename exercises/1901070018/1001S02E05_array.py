li = []
for i in range(0, 10):
    li.append(str(i))
li.reverse()
st = ''
st1 = st.join(li)
st2 = st1[2:10]
li2 = sorted(st2,reverse=False)
st3 = st.join(li2)
st4 = int(st3)
binary = bin(st4)
octal = oct(st4)
hexadecimal = hex(st4)
print('二进制数：{},\t八进制数：{},\t十六进制数：{}'.format(binary, octal, hexadecimal))