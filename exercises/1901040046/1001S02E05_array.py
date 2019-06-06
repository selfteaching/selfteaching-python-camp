a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
print(a)

s = "".join(map(str,a))
s1 = s[2:8]
s2 = s1[::-1]
s3 = int(s2)
print(s3,"二进制是：",bin(s3))
print(s3,"八进制是：",oct(s3))
print(s3,"十六进制是：",hex(s3))
