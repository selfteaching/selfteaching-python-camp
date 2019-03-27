#  控制流程学习程序
# 功能1 ：用 for……in ……完成九九表打印
# 功能2 ：用while打印九九表，并用条件判断把偶数行除掉
# 第四天的作业
#  2019.3.24
# --------------
# n_1：乘数1， n_2：乘数2 
# 用 for……in ……完成九九表打印
print('The first: \n')
for n_1 in range(1, 10):
	for n_2 in range(1, n_1+1):
		print(n_1, '*', n_2, '=', n_1*n_2,end='\t')
	print()


# 用 用while打印九九表，并用条件判断把偶数行除掉
print('\n-------------\nThe second: \n')
n_1=1
while n_1<10:
	n_2 = 1
	while n_2 < n_1+1:
		#除掉偶数行
		if not(n_1 % 2 == 0):
			print(n_1, '*', n_2, '=', n_1*n_2,end='\t')
		n_2 = n_2+1
	print()
	n_1 = n_1+1
