
# from IPython.core.interactiveshell import InteractiveShell
# InteractiveShell.ast_node_interactivity = "all"

array = [0,1,2,3,4,5,6,7,8,9]
array.reverse()
s = ''.join(map(str,array))
s1 = s[2:8]
result = s1[::-1]
dec = int(result)
print("十进制数为：", dec)
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))