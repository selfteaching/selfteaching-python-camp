shuzu=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
shuzu.reverse() 
print(shuzu)


s = ''
for i in range(0,10):
    shuzu[i]=str(shuzu[i])
zifuchuan=s.join(shuzu)
print(zifuchuan)

r1=zifuchuan[2:8] 
print(r1)
zhengshu=int(r1[::-1])
print(zhengshu)
print(bin(zhengshu))
print(oct(zhengshu))
print(hex(zhengshu))
