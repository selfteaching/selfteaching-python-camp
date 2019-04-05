print("封装统计英文单词词频的函数")
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
def stats_text_en(string):                  #统计英文词频
    import re                               #导入正则表达式模块
    list1 = re.split(r'\W+',string)         #将字符串转换为只保留单词为元素的列表
    while '' in list1:               
        list1.remove('')                    #删除list1中为空的元素
    dict1 = {}                              #建立空字典
    for i in list1:                         #i属于list1中的元素，开始循环
        dict1.setdefault(i,list1.count(i))  #将列表中的单词及单词的出现次数分别赋值给dict1中的键和值
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)    #将dict1按照value值从大到小排列，并将结果赋值给元祖tup1
    return tup1                             #返回tup1的值
result = stats_text_en(text)
print(result,end='\n\n')




print("封装统计中文汉字字频的函数")
text = '''
观自在菩萨，行深般若波罗蜜多时，照见五蕴皆空，渡一切苦厄。
舍利子!色不异空，空不异色;色即是空，空即是色;受想行识，亦复如是。
舍利子!是诸法空相，不生不灭，不垢不净，不增不减。
是故空中无色，无受想行识，无眼耳鼻舌身意，无色声香味触法，无眼界，乃至无意识界。
无无明，亦无无明尽，乃至无老死，亦无老死尽，无苦集灭道。无智亦无得。
以无所得故，菩提萨埵，依般若波罗蜜多故，心无罣碍，无罣碍故，无有恐怖， 远离颠倒梦想，究竟涅槃。
三世诸佛，依般若波罗蜜多故，得阿耨多罗三藐三菩提。
故知般若波罗蜜多，是大神咒，是大明咒，是无上咒，是无等等咒，能除一切苦，真实不虚。
故说般若波罗蜜多咒，即说咒曰︰揭諦揭諦，波罗揭諦，波罗僧揭諦，菩提娑婆呵。
'''
#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
def stats_text_ch(text):
  dictionary={}                        #引用一个空字典
  for i in text:
     if u'\u4e00' <= i <= u'\u9fa5':   #提取中文汉字   
         dictionary[i]=text.count(i)
  return dictionary
frequency = stats_text_ch(text)
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))
