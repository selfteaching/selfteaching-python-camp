data = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(data)
data.reverse()
print(data)

string = ''.join(str(i) for i in data)
print(string)
string_p1=string[2:8]
print(string_p1)
string_p2 = string_p1[::-1]
print(string_p2)

data1 = int(string_p2)
print(bin(data1))
print(oct(data1))
print(hex(data1))