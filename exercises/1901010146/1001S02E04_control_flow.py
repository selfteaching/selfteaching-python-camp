#以下为1.0版本
#i=1
#j=1
#for i in range(i,9,1):
#	j=1
#	for j in range(j,i,1):
#		print(i,'*',j,'=',i*j,end='\n')

#以下为2.0版本
print("以下是使用for语句实现的九九表：")
i=0
j=1
for i in range(i,10,1):		#结束值由9变成了10，说明值为9时，数值只停止到8
	j=1
	print()		#单纯的换行功能
	for j in range(j,i+1,1): 	 #i+1解决了没有n*n的问题
		a = i*j
		if a < 10:		#这个条件语句，解决了输出错位的问题
			print(i,'*',j,'= ',i*j,'  ',end='')
		else:
			print(i,'*',j,'=',i*j,'  ',end='')

print('\n'*2)
print("以下是使用while语句实现的九九表：")

i = 1
j = 1
while i < 10:
	j = 1
	print()
	while j <= i:
		a = i * j
		if a < 10:		#这个条件语句，解决了输出错位的问题
			print(i,'*',j,'= ',i*j,'  ',end='')
		else:
			print(i,'*',j,'=',i*j,'  ',end='')
		j += 1
	i += 1
	