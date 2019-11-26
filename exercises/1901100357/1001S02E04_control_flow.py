# print times tables with for...in


for x in range(1,10):
	for y in range(1, x+1):
		print('%d*%d=%d'%(x, y, x*y), end='\t')
	print('')

# print times tables2 with while

a = 0
while a < 10:
	a += 1
	if a%2 == 0:
		continue
	else:	
		b = 1
		while b < a+1:
			print('%d*%d=%d'%(a, b, a*b), end='\t')
			b += 1
		print('')
	

