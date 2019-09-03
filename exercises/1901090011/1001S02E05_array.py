array=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#AI-1.Reverse the array

array.reverse()

#AI-2.Join them in string

str1=''.join(str(i) for i in array)

#AI-3.Take the 3rd to 8th in the string
str2=str1[2:8]

#AI-4.Reverse the string
str3=str2[::-1]

#AI-5.Int the string
int1=int(str3)

#AI-6.Binary, Oct & Hex
Bin=bin(int1)
Oct=oct(int1)
Hex=hex(int1)
print(Bin)
print(Oct)
print(Hex)