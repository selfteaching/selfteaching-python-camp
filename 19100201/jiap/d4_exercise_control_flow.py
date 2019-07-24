# This is ex4 for control flow
#-*- coding:utf-8 -*-
print("9*9 Multiple formula")

for num_a in range(1, 10):
	for num_b in range(1, num_a+1):	
		if num_b == num_a:
			endstr	= "\n"
		else:
			endstr = "\t"
		print("%d * %d = %d" % (num_b, num_a, num_a * num_b), end = endstr)

# 这里使用了 if 语句去控制print() 最后的输出结果。

print("\n----------------------------------------------\n")

print("9*9 Multiple formula(except even numbers)")

num_c = 1
while (num_c < 10) :
	num_d = 1
	while (num_d <= num_c):
		
		if num_c == num_d:
			endstr	= "\n"
		else:
			endstr = "\t"

		print("%d * %d = %d" % (num_c, num_d, num_c * num_d), end=endstr)
		num_d += 1

	if (num_c % 2 == 0):
		num_c += 1
	else:
		num_c += 2









