
# copied @echojce 19100101 and not wholy understood yet
# tried to convert into some part of mine
# assign a value to my_arr
my_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# using .reverse() method
my_arr.reverse()
# to check the result using: print('Here comes my reversed array: ', my_arr)
# converting the reversed array into strings 将翻转后的数组拼接成字符串
my_str1 = ''.join(str(i) for i in my_arr)
# 用字符串切片的方式取出第三个到第八个字符（包含第三和第八个字符）
my_str2 = my_str1[3:9]
# 将获得的字符串进行反转
my_str3 = my_str2[::-1]
# 将结果转为int型
my_int1 = int(my_str3)
# converting to binary/octonary/hexadecimal number
# print out 3 number systems results
# checking by: print('decimalism: ', my_int1)
print('Converting to binary system: ',bin(my_int1))
print('Converting to octonary number system: ',oct(my_int1))
print('Converting to hexadecimal number system: ',hex(my_int1))