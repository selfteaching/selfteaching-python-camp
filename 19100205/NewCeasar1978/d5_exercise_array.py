a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
a.reverse()
print(a)
text = ''
for i in a:
    j = str(i)
    text += j

print(text)

text = text[2:8]

text = text[::-1]

i = int(text)

print(bin(i).replace('0b',''))
print(oct(i))
print(hex(i))