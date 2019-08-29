text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# better 被替换为 worse
t_h = text.replace("better","worse")    
print(t_h)

# 将单词中包含 ea 的单词剔除
fen_ge = t_h.split(' ')       #通过空格, 把字符串分割 为单个元素 的列表
# print(fen_ge)
new1 = []            # 定义一个新列表,以便操作,存储新的元素
for m in fen_ge  :      # 取出每一个单词 给变量 A
     if "ea" not in m :     # 如果ea 不在 这个单词里
        new1.append(m)     # 新列表末尾 增加这个元素
print(new1)     

""" 
第二种方法 find 的用法
# 用 for ... in 循环遍历一遍 f_g 里的元素, 然后判断单词变量A 是否包含 ea
for A in fen_ge:
    # str 类型 的 find 方法 如果不包含 参数 字符则返回 -1, 如果包含则返回改字符第一次出现的索引
    if m.find('ea') < 0:
        new1.append(m)
print('将单词中包含 ea 的单词删除 ==>', new1)
 """


#大小写翻转    
# 这里最大的一个坑,就是 大小写翻转的操作对象只能是 字符串; list类型无法翻转
new2=' '.join(new1)    # 先拼接 列表元素为 一个字符串,该函数功能和spilt() 相反
new3=new2.swapcase()    # 大小写 相互转换
print(new3)



#将所有单词按照a...z升序排列
# 这里有一个大坑,: 排序的操作对象只能是 list 类型,字符串无法进行排序
fen_ge1 = new3.split(' ')       #再次 通过空格, 把字符串 分割 为单个元素 的列表
# print(fen_ge1)

fen_ge1.sort()        # sort 默认进行的就是 升序排列,当然还有降序 
# print(fen_ge1)

pin_jie=' '.join(fen_ge1)   # 再次转换为 字符串
print(pin_jie)

"""
 如果 调整一下做题顺序 : worse 替换 better 后,是字符串
 先进行 大小写翻转,
 在提出 含有ea 的单词 ,此时是 list 
 最后进行升序排列 ,这样也可以实现
 尽管麻烦一些,但是 遇到了数据类型 无法进行下一步操作,会报错,自己学会了看,并去找原因,这个才是最重要的 技能
 """