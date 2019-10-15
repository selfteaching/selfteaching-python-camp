a=[0,1,2,3,4,5,6,7,8,9]
b=sorted(a,reverse=True)
print('翻转过后:',b)
c=''.join([str(i) for i in b])
print('转为字符串',c)
d=c[2:8]
print('切片后:',d)
print('翻转：',d[::-1])
e=int(d)
print('int类型：',e)
print('二进制：',bin(e))
print('八进制：',oct(e))
print('十六进制:',hex(e))