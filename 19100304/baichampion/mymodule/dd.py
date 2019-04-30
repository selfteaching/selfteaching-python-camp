import re
ttt = '''
love in china 我爱中国
'''
s = re.findall('[a-zA-Z]+',ttt)
b = ' '.join(s)
print(b)