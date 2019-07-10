a_list=[0,1,2,3,4,5,6,7,8,9]
a_list.sort(reverse=True) #reverse 参数，默认是 False
#print('the list sorted reversely:\n', a_list)

#print()
#转为字符串
b_list=[]
for i in a_list:
    j=str(i)
    b_list+=j
#print(b_list)

#print()
#第三到第八个字符
m=b_list[2:8]
#print(m)

#print()
#翻转
m.sort()
#print(m)

#print()
#int输出
s=[]
for n in m:
    p=int(n)
    s.append(p)
#print(s)

#print()
#二进制：bin(),八进制：oct(),十六进制：hex()

#二进制
k=[]
for q in s:
    j=bin(q)
    k.append(j)
print(k)

print()
#八进制
k=[]
for q in s:
    j=oct(q)
    k.append(j)
print(k)

print()
#十六进制
k=[]
for q in s:
    j=hex(q)
    k.append(j)
print(k)