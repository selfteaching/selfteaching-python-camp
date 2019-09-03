nums = [0,1,2,3,4,5,6,7,8,9]   

nums.reverse()

nums_new = [str(x) for x in nums]

nums_new = "".join(nums_new)

nums_new_38 = nums_new[2:8]

nums_new_38 = int(nums_new_38[::-1])

print("转换为二进制为：", bin(nums_new_38))
print("转换为八进制为：", oct(nums_new_38))
print("转换为十六进制为：", hex(nums_new_38))