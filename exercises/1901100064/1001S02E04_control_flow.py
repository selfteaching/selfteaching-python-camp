
# 练习for in 循环
# 练习if，elif,else选择语句
# 使用了break语句
#  使用了range() 函数
for i in range(1,10,1):
	for j in range(1,10,1):
		if j<i :
			print(i,'*',j,'=',i*j,end='\t')
		elif j==i :
			print(i,'*',j,'=',i*j)
		else :
			break

print('----'*10)

# 练习while循环，else语句
# 练习if，elif,else选择语句
# 使用了break语句
i = 1
j = 1
while i<=9 :
    if i%2 !=0 :     
        while j<=9:
            if j < i :
                print(i,'*',j,'=',i*j,end='\t')
                j =j +1
            elif j==i:
                print(i,'*',j,'=',i*j)
                j =j +1
            else:
                j =1
                break
    else:
        pass
    i=i+1


