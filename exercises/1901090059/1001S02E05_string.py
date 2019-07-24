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
There should be one-- and preferably only one --obvious way to do it. 
Although that way may not be obvious at first unless you're Dutch. 
Now is better than never. 
Although never is often better than *right* now. 
If the implementation is hard to explain, it's a bad idea. 
If the implementation is easy to explain, it may be a good idea. 
Namespaces are one honking great idea -- let's do more of those!
'''
#1.将字符串样本里的 better 全部替换成 wrose

#调用 Str 类型的 replace 方法进行替换
textBetterRepWorse = text.replace('better', 'worse')
print("将字符串样本里的 better 全部替换成 worse ==>",textBetterRepWorse)

#2。 将单词中包含 ea 的单词删除

#先将字符串根据 空白字符 分割成 list， 要调用 str 类型
textRemoveWordsInea = textBetterRepWorse.split()

#定义一个 list 类型的变量用来存放过滤完的单词
textRemoveWordsIneaS = []
"""
for a in textRemoveWordsInea:
    if 'ea' in a:
        a = a.rstrip('.')
      #  print(a)
        textRemoveWordsIneaS = textRemoveWordsIneaS.replace(a, '')
"""
# 用 for  ... in 循环遍历一遍 textRemoveWordsInea 然后判断单词是否包含ea
for word in textRemoveWordsInea:
  if word.find('ea') < 0:
      textRemoveWordsIneaS.append(word)
print("将单词中包含ea的单词删除===>", textRemoveWordsIneaS)

#3. 进行大小写翻转
# 利用 列表推倒式 对 str 类型的元素进行大小写翻转
RevertextRemoveWordsIneaS = [i.swapcase() for i in textRemoveWordsIneaS ]
#RevertextRemoveWordsIneaS = textRemoveWordsIneaS.swapcase() #错误是因为List的操作
print("进行大小写翻转 ==>", RevertextRemoveWordsIneaS)

#4. 单词按 a..z 升序排列
#SortRevertextRemoveWordsIneaS = RevertextRemoveWordsIneaS.split()
#SortRevertextRemoveWordsIneaS.sort()
print("单词按照 a..z 升序排列 ==>", sorted(RevertextRemoveWordsIneaS))




