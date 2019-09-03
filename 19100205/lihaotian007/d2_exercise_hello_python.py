# 这是用于打印“Hello World” 的程序
#meg = "Hello World" #创建一个变量meg
#print(meg) #打印变量meg的内容

#day 6 测试内容
""""
def ceshi(a = 0) :
    return a+1

list_a = []
for i in range(1,10) :
    list_a.append(ceshi(i))

print(list_a)
"""

#day 9 测试内容

#list_a = []
#import collections as coll
#x = coll.Counter(['red', 'blue'])
#c['red', 'blue', 'yello']

#y = coll.Counter(a = 4, b = 2, c = 6, d = -1)
#print(y.elements())
#print(list(y.elements()))
#print(str(y.elements()), '\n')
#z = coll.Counter('12345678132456575465')
#print(z.elements())
#print(list(z.elements()))
#print(str(z.elements()))
# print(dict(y.elements()))
#list_a = y.elements()
#print(list_a)
#print(sorted(y.elements()))
#print(y,'\n')

#dict_b = {'a':1, 'b':2, 'c':3}
#print(sorted(dict_b.items(), key = lambda x:x[1], reverse = True))
#print(x.most_common())
"""
print(x)
x['yellow'] += 2
print(x)
x['yellow'] = 4
print(x,'\n')
x['prower'] = -2
#print(sum(y.values()))
print(x.most_common(2)[:-2-1:-1])
print(x)

y = coll.Counter(['red', 'blue'])
print(y)
print(x+y)
"""

# day 10 测试
"""
import jieba
print('开始：\n\n')
seg_list = jieba.cut("今天的天气很好，可惜没能出去")
print(seg_list)
seg_list1 = "/".join(jieba.cut("今天的天气很好，可惜没能出去"))
print(seg_list1)
seg_list2 = list("/".join(jieba.cut("今天的天气很好，可惜没能出去")))
print(seg_list2)
#seg_list3 = dict("/".join(jieba.cut("今天的天气很好，可惜没能出去")))
#print(seg_list3)
seg_list4 = str("/".join(jieba.cut("今天的天气很好，可惜没能出去")))
print(seg_list4)

with open('D:\\GitHub - Desktop\\selfteaching-python-camp\\19100205\\lihaotian007\\mymodule\\tang300.json','r',encoding = 'UTF-8') as op_tang :
    read_tang = op_tang.read()
    print(read_tang)
op_tang.closed

list_a = ['1','2','3']
print('结果是：',str(list_a))
"""

# day 11 测试

list_a = [(1,2),(2,3),(3,4)]
print(len(list_a[1]))
from itertools import chain
b = list(chain.from_iterable(list_a))
print(b)