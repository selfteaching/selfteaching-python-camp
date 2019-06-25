def cool(x,y):
    return (x*y)
print("赶紧输入第一个数字:")
a=int(input(''))
print('请选择：+，-，*，/')
c=input('')
print('请输入第二个数字:')
b=int(input(''))
if c=='*':
    print(cool(a,b))
else:
    print("请重新输入")
    
    