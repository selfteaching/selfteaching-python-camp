
def takeSecond(elem):
    return elem[0]
 
# 列表
random = [(2, 2), (3, 4), (4, 1), (1, 3)]
 
# 指定第二个元素排序
random.sort(key=takeSecond)
 
# 输出类别
print ('排序列表：', random)





for col in range(1,10):
    for row in range(1,col+1):
        print(str(col),"*",str(row),'=',row*col,' ',end='')
    print()





r=1
while r<=9:
    c=1
    while c<=r and (r%2!=0):
        print(str(r),"*",str(c),"=",c*r,' ',end='')
        c=c+1
    print()
    r=r+1    
    

