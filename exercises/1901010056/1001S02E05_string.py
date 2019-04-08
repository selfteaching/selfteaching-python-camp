text = ''' The Zen of Python, by Tim Peters 
Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! '''
#里面的text的行数似乎对于函数的运行也有影响

#将字符串样本text里的 better 全部替换成 worse 
text = text.replace('better', 'worse')  #str.replace(old, new[, count]).式子里的小点，可以理解为操作符，从其他模块调用函数

#将单词中包含 ea 的单词剔除 
#不要用 list 作为变量，可以用以下变量名，如 list_text, list_1, my_list 等 
textlist1 = text.split()   #通过 string 的 split() 将字符串切成数组

str1 = []                  #表示定义一个列表，str是文本序列类型，字符串。列表推导用方括号（“[]”）括起来
#在C语言中数组 int nums[]={1,2,3,4,5}C语言数组必须是什么类型就是什么类型，Python列表可以储存任何类型的数组

str2 = 'ea'                  
for i in textlist1:        #里面的i 不需要定义吗？
    if str2 not in i:      #注意带上冒号
        str1.append(i)    #str1.append表示添加i到原来列表str1的最后。注意相对于上一行的位置
#列表的其他应用str1.insert(1,"e")  表示就是在列表str1第一个位置插入e
# str1.pop表示从后往前删除，删除最后一个。根据栈的特点，先进后出，后进先出。str.remove(a)表示删除str1表中的a                    
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