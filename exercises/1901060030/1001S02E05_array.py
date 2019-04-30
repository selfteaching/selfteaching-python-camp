print("Number operation")
List = [0,1,2,3,4,5,6,7,8,9]

print("\nTask 1: reverse the list")
List.sort(reverse=True)
print(List)
print(type(List))

print("\nTask 2: convert list to string and join all the strings")
New_list = [str(i) for i in List]
s = ''
s = s.join(New_list)
print(s)
print(type(s))

print("\nTask 3: slicing out 3rd to 8th character")
q = s[2:8]
print(q)
print(type(q))

print("\nTask 4: reverse again!")
New_list2 = []
for i in q:
    New_list2.append(i)
print(New_list2.sort())


print("\nTask 5: convert to Int")
p = ''
p = p.join(New_list2)
print(p)
r = int(p)
print(type(r))

print("\nTask 6: convert to Binary, Octal, and Hexadecimal")
r_bin = bin(r)
print("Binary: ", r_bin)
r_oct = oct(r)
print("Octal: ", r_oct)
r_hex = hex(r)
print("Hexadecimal: ", r_hex)