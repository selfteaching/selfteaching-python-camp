text = ''' The Zen of Python, by Tim Peters 
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''
#里面的text的行数似乎对于函数的运行也有影响

#将字符串样本text里的 better 全部替换成 worse 
text = text.replace('better', 'worse')  #str.replace(old, new[, count]).

#将单词中包含 ea 的单词剔除 
textlist1 = text.split()   #拆分字符串,split就是分裂的意思。弄成''的形式，这是要删除单词前需要的步骤
str1 = []                  #赋予这个作用是什么？str是什么意思？str是文本序列类型，字符串中定义的常量
str2 = 'ea'
for i in textlist1: 
    if str2 not in i: #注意带上冒号
        str1.append(i) #里面的append函数还需要了解。str.append相当于定义字符串str1为附件函数。注意相对于上一行的位置
                       ##append the object to the end of the list
#print(textlist1)

#将字母进行大小写翻转
textlist2 = []              #列表推导用方括号（“[]”）括起来。生成器表达式用括号（“（）”）括起来
for i in textlist1:
    i = i.swapcase()       #将i的字母进行反转
    textlist2.append(i)    #textlist2是append的i
#print(textlist2)

#将单词按升序排列，并输出结果
textlist2.sort()    #sort(*, key=None, reverse=False)此方法会对列表进行原地排序，只使用 < 来进行各项间比较
print(textlist2)    #key 指定带有一个参数的函数，用于从每个列表元素中提取比较键 (例如 key=str.lower)。
                    #对应于列表中每一项的键会被计算一次，然后在整个排序过程中使用。 默认值 None 表示直接对列表项排序而不计算一个单独的键值。
                    #reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序