from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'

a_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
#print( f'a_list =', a_list )
b_list = a_list.copy()
#print(f'b_list =', b_list)
b_list.reverse()
#print( f'b_list =', b_list )

# 将 b_list 中的整数转换成字符类型，便于后续进行字符串拼接
b_list_str = []
for i in range( len(b_list) ):
    b_list_str.append( str(b_list[i]) )
#print( f'b_list_str = ', b_list_str )

s = ''
b_join = s.join( b_list_str )
#print( f'翻转后的数组拼接成字符串为：', b_join )

b_join_part = b_join[2:8]
#print( f'提取 {b_join} 的第3到8个字符：', b_join_part )

# 字符串没有reverse()Method，只能通过使用循环来翻转
l = len(b_join_part)
for i in range( l ):
    s += b_join_part[l-i-1]
#print( f'将 {b_join_part} 翻转：', s )

s_int = int(s)
print(f'十进制形式：', s_int)

s_bin = bin(s_int)
s_oct = oct(s_int)
s_hex = hex(s_int)

print( f'{s} 的二进制形式：', s_bin )
print( f'{s} 的八进制形式：', s_oct )
print( f'{s} 的十六进制形式：', s_hex )