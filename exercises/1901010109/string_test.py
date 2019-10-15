from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

# str.find(sub[, start[, end]])
print('Example of str.find():')
s = """Simple is better than complex.。！`!
Complex is better than complicated."""
a = s.lower().find('mpl')
b = s.lower().find('mpl', 10)
c = s.lower().find('mpl', 10, 20)
print(a,b,c,sep='\n')

# str.startswith(prefix[, start[, end]])
print("s.lower().startswith('s'):",\
    s.lower().startswith('s', 0))
print("s.lower().startswith('i')",\
    s.lower().startswith('i', 7))
print("s.lower().startswith('co', 31, 40)",\
    s.lower().startswith('co', 31, 40))

print(f's：', s)
symbols = ',.-:;!@#$%^&*()-+=<>?/`~|[]{}，。？、·~！@#￥%……&*（）——+-={}【】、|；：“”‘’'
for symbol in symbols:
    s = s.replace(symbol, '')


s1 = s.replace( 't', '' )
print(f'去掉标点符号：', s1)
