#用函数做词频统计
'''text = 愚公移山
太行，王屋二山的北面，住了一個九十歲的老翁，名叫愚公。二山佔地廣闊，擋住去路，使他和家人往來極為不便。
一天，愚公召集家人說：「讓我們各盡其力，剷平二山，開條道路，直通豫州，你們認為怎樣？」
大家都異口同聲贊成，只有他的妻子表示懷疑，並說：「你連開鑿一個小丘的力量都沒有，怎可能剷平太行、王屋二山呢？況且，鑿出的土石又丟到哪裏去呢？」
大家都熱烈地說：「把土石丟進渤海裏。」
於是愚公就和兒孫，一起開挖土，把土石搬運到渤海去。
愚公的鄰居是個寡婦，有個兒子八歲也興致勃勃地走來幫忙。
寒來暑往，他們要一年才能往返渤海一次。
住在黃河河畔的智叟，看見他們這樣辛苦，取笑愚公說：「你不是很愚蠢嗎？你已一把年紀了，就是用盡你的氣力，也不能挖去山的一角呢？」
愚公歎息道：「你有這樣的成見，是不會明白的。你比那寡婦的小兒子還不如呢！就算我死了，還有我的兒子，我的孫子，我的曾孫子，他們一直傳下去。而這二山是不會加大的，總有一天，我們會把它們剷平。」
智叟聽了，無話可說：
二山的守護神被愚公的堅毅精神嚇倒，便把此事奏知天帝。天帝佩服愚公的精神，就命兩位大力神揹走二山The Zen of Python, by Tim Peters Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. Flat is better than nested. Sparse is better than dense. Readability counts. Special cases aren't special enough to break the rules. Although practicality beats purity. Errors should never pass silently. Unless explicitly silenced. In the face of ambxiguity, refuse the temptation to guess. There should be one-- and preferably only one --obvious way to do it. Although that way may not be obvious at first unless you're Dutch. Now is better than never. Although never is often better than *right* now. If the implementation is hard to explain, it's a bad idea. If the implementation is easy to explain, it may be a good idea. Namespaces are one honking great idea -- let's do more of those! xx xxx xx xxx aa a aa a a a a a a xx xxx..;.;.;今天我吃饭了，今天我洗脸了，今天我吃汉堡了，明天我再也不想吃了a-zA-Z]+[\'\-]?[a-zA-Z'''

#调用Counter功能
from collections import Counter

#引用“结巴”中文分词
import jieba

#引用re
import re

#英文词频排序
def stats_text_en(text1):
    #创建一个字典
    #count = {}

    # 把字符串去掉转行、大写换小写、去掉单词两边字符
    #text = text1.replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','').lower().split(' ')

    #筛选出英文字母和字符   
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    text_en = re.findall(en_pattern, text1)

    # 如果字典里有该单词则词频+1，否则添加入字典(day6)
    '''for word in text_en:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word] = 1
    #按照词频从高到低排列
    count_list = sorted(count.items(),key=lambda a:a[1],reverse=True)'''

    #用counter优化输出(day9)
    count_list = Counter(text_en).most_common(0)

    return count_list
#print ("单词出现频率排列如下：",state_text_en(text))


#中文字频排序
def stats_text_cn(text2):

    #建立列表
    cut_list = []
    word_list = []
    count_list = []

    #去掉符号    
    #text = text2.replace('—','').replace(' ','').replace(',','').replace('.','').replace(':','').replace(';','').replace('"','').replace('!','').replace('?','').replace('、','').replace('，','').replace('。','').replace('“','').replace('”','').replace('：','').replace('；','').replace('\n','').replace('！','').replace('？','').replace('/','')
    
    #建立字典
    #count = {}

    #筛选出汉字   
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    text_cn = re.findall(cn_pattern, text2)

    #把筛选返回的list转为str
    text_cut = ''.join(text_cn)

    #使用jieba精准模式分词
    cut_list = jieba.lcut(text_cut,cut_all=False)

    #筛选大于等于2字的词
    for word in cut_list:
        if len(word) >= 2:
            word_list.append(word)

    '''#用for循环做字频统计(day6)
    for word in text_cn:
        if word in count.keys():
            count[word] = count[word] + 1
        else:
            count[word]=1
    #调整排序并输出
    count_list = sorted(count.items(),key=lambda a:a[1],reverse=True)'''

    #用counter优化输出(day9)
    count_list = Counter(word_list).most_common(10)

    return count_list
#输出
#print ("字出现频率排列如下：",state_text_cn(text))

#定义stats_text函数，合并输出
def stats_text(text):

    #用isinstance（变量名，类型）判断字符串类型是否正确，如果不正确抛出ValueError
    if isinstance(text,str) != True:
        raise ValueError
    else:
        return (stats_text_en(text) + stats_text_cn(text))

#print ("单词出现频率排列如下：",stats_text(text))