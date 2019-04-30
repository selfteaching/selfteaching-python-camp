# 19100304 day6 银零
#【assignment1：封装统计英文单词词频的函数】
#【assignment2：封装统计中文汉字字频的函数】



text_en = '''
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
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than right now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''

text_cn = '''
PHP 是你的豆蔻年华的心上人，她是情窦初开的你今年夏天傻乎乎的追求的目标。玩一玩可以，但千万不要投入过深，因为这个女孩有严重的问题。
Ruby 是脚本家族中一个非常漂亮的孩子。第一眼看她，你的心魄就会被她的美丽摄走。她还很有有趣。起初她看起来有点慢，不怎么稳定，但近些年来她已经成熟了很多。
Python 是 Ruby 的一个更懂事的姐姐。她优雅，新潮，成熟。她也许太过优秀。很多小伙都会说“嘿，兄弟，你怎么可能不爱上 Python 呢！？”。没错，你喜欢 Python。你把她当成了一个脾气和浪漫都退烧了的 Ruby。
Java 是一个事业成功的女人。很多在她手下干过的人都感觉她的能力跟她的地位并不般配，她更多的是通过技巧打动了中层管理人员。你也许会认为她是很有智慧的人，你愿意跟随她。但你要准备好在数年里不断的听到“你用错了接口，你遗漏了一个分号”这样的责备。
C++ 是 Java 的表姐。她在很多地方跟 Java 类似，不同的是她成长于一个天真的年代，不认为需要使用“保护措施”。当然，“保护措施”是指自动内存管理。你以为我指的是什么？
C 是 C++ 的妈妈。对一些头发花白的老程序员说起这个名称，会让他们眼睛一亮，产生无限回忆。
Objective C C 语言家族的另外一个成员。她加入了一个奇怪的教会，不愿意和任何教会之外的人约会。
'''


#【assignment1：封装统计英文单词词频的函数】
# 1.定义一个名为 stats_text_en 的函数，函数接受一个字符串为参数
# 2.实现该函数的功能（同day5 任务2）：统计参数中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
# 3.为 stats_text_en 添加注释说明

def stats_text_en(string):
    import re                                       #导入正则表达式模块
    list1 = re.split(r'\W+',string)                 #将字符串转换为列表list1，只保留单词为list1中的元素
    while '' in list1:                              #删除list1中为空的元素
        list1.remove('')
    dict1 = {}                                      #建立空的字典
    for i in list1:                                 #i属于list1中的元素，开始循环
        dict1.setdefault(i,list1.count(i))          #将列表中的单词及单词的出现次数，分别赋值给dict1的键和值
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)             #将dict1按照value值从大到小排列，并将结果赋值给元祖tup1
    return tup1                                     #返回tup1的值

result = stats_text_en(text_en)
print(result,end='\n\n')


#【assignment2：封装统计中文汉字字频的函数】
# 1.定义一个名为 stats_text_cn 的函数，函数接受一个字符串为参数
# 2.实现该函数的功能：统计参数中每个中文汉字出现的次数，最后返回一个按字频降序排列的数组
# 3.为 stats_text_cn 添加注释说明

def stats_text_cn(string):
    import re                                       #导入正则表达式模块
    result_cn_interpunction = re.sub('[^\u4e00-\u9fa5]','',string)                      #提取中文字符串
    string = string.replace(' ','').replace('\n','')#删除空元素与换行元素
    list1 = re.split('',string)                     #将字符串转换为列表list1
    dict1 = {}                                      #建立空的字典
    for i in list1:                                 #i属于list1中的元素，开始循环
        dict1.setdefault(i,list1.count(i))          #将列表中的汉字及汉字的出现次数，分别赋值给dict1的键和值
    tup1 = sorted(dict1.items(),key = lambda items:items[1],reverse = True)             #将dict1按照value值从大到小排列，并将结果赋值给元祖tup1
    return tup1                                     #返回tup1的值

result = stats_text_cn(text_cn)
print(result)


