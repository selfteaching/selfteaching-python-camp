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
'''处理英文文本,按照单词出现次数,输出从大到小排序结果'''
import collections
def stats_txt_en(text):#处理英文文本,按照单词出现次数,输出从大到小排序结果
    dicta={}
    count=100
    if type(text) == str:#添加字符串类型检查
        text=text.replace(',',' ').replace('.',' ').replace('--',' ').replace('!',' ').replace('*',' ') #替换所有标点符号为空格
        text=text.lower()  #统一成小写
        text=text.split()  #切割字符串
        for i in text:
            dicta[i]=text.count(i)
        dicta=collections.Counter(dicta).most_common(count) #按照单词出现次数，从大到小排序
        print(dicta)
    else:
        raise ValueError('不是字符串，请重新输入！')

stats_txt_en(text)

text1 = '''
此开卷第一回也。作者自云：曾历过一番梦幻之后，故将真事隐去，而借
通灵说此《石头记》一书也，故曰“甄士隐”云云。但书中所记何事何人?自己又
'''

'''处理文本,按照汉字出现次数,输出从大到小排序结果'''
import re
import jieba
def stats_txt_cn(text1):
    ''' day10 使用jieba第三方库统计长度大于等于2的中文词汇出现频率 '''
    count=100
    if type(text1) == str:
        txtlist = re.findall(u'[\u4e00-\u9fff]+', text1.strip())  # 提取中文
        text2 = ''.join(txtlist) 
        txtlist1 = [ i for i in jieba.cut_for_search(text2) if len(i) >= 2]
        return collections.Counter(txtlist1).most_common(count)#为中文字计数，返回中文字及所计数
    else:
        raise ValueError("不是字符串，请重新输入！")
stats_txt_cn(text1)

'''
day9 作业
    count=100
    if type(text1) == str:
        txtlist = re.findall(u'[\u4e00-\u9fff]+', text1.strip())  # 提取中文
        text1 = ''.join(txtlist) 
        return collections.Counter(text1).most_common(count)
        #为中文字计数，返回中文字及所计数
'''
'''
以下为第9天一直没搞通的程序，思路有问题，改思路，不用去除的方法了。
def stats_txt_cn(text1):#处理中文文本
    if type(text1) == str:#添加字符串类型检查
        word_lst = []
        word_dict = {}
        count=100
        p =  re.compile(r'[\n|「」\·~\！\@#\￥\%\……\&*\（\）\——-+\=\【\】{}\、|\；\‘\’\：\“\”\《\》\？\，\。\、`~ !\@#\$\%\^\&*()_+-\=[]{}\|\;\'\'\:\"\"\,.\/\<>\?a-zA-Z0-9 ]')
        text1 = re.sub(p, '', text1)
        # 添加每一个字到列表中
        for line in text1:
            for char in line:
                word_lst.append(char)
        # 用字典统计每个字出现的个数       
        for char in word_lst:
            if char.strip() not in word_dict: # strip去除各种空白
                word_dict[char] = 1
            else :
                word_dict[char] += 1
        lstWords = collections.Counter(word_dict).most_common(count) #按照单词出现次数，从大到小排序
        print(lstWords)

    else:
        raise ValueError('不是字符串，请重新输入！')    
stats_txt_cn(text1)

'''
'''英汉合并词频统计'''

def stats_text(text):
    if type(text) == str:#添加字符串类型检查
        print(stats_txt_en(text))
        print(stats_txt_cn(text))
    else:
        raise ValueError('不是字符串，请重新输入！') 
stats_text(text)