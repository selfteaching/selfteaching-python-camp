a=[]
for i in range(10):
	a.append(i)
a.reverse()
print(a)

s=''
for i in a:
	s+=str(i)
print(s)

ac = s[2:8]
print(ac,'is the converted integer')

acr = ac[::-1]

x = int(acr)

print(bin(x),"in binary.")
print(oct(x),"in octal.")
print(hex(x),"in hexadecimal.")

