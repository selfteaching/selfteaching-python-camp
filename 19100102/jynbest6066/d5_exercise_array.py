a1 = [1,2,3,4,5,6,7,8,9]
a1.reverse()

s1 = ''.join(map(str,a1))   

s2 = s1[2:8]

s3 = s2[::-1]

s4 = int(s3)

print(s4,"二进制：",bin(s4))
print(s4,"八进制：",oct(s4))
print(s4,"十六进制：",hex(s4))