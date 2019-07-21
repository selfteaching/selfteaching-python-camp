m = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
m.reverse()
print(m)
m1 = [str(i) for i in m]
m2 = ''.join(m1)
print(m2)
m3 = m2[2:8]
print(m3)
m4 = m3[::-1]
print(m4)
m5 = int(m4)
print(m5)
print('二进制：', bin(m5))
print('八进制：', oct(m5))
print('十六进制：', hex(m5))
