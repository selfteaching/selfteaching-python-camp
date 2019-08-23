def stats_text_en(text):  #自定义函数，该函数用于统计参数text中每个英文单词出现的次数，最后返回一个按词频降序排列的数组
    text1 = text.split()    #把字符串变成list格式
    text2 = []  #新建一个列表，用于存入处理过后的str          
    symbols = ",.-!*"   #整理出文本中需要剔除的符号
    for En in text1:    #在列表text1中遍历所有字符
        for symbol in symbols:  #如果包含symbols中需要剔除的字符，用replace语句替换掉
            En = En.replace(symbol, "")
        if len(En): #剔除了字符后如果单词En的长度不为0，那么就算正常单词，可以加入到新的列表中
            text2.append(En)
    #先把text中的符号剔除掉
    text3 = " ".join(text2)
    text3 = text3.lower()   
    #把所有的单词变成小写格式
    text3 = text3.split()  
    #把text变成list格式
    d = {}   
    #采用空字典形式保存结果
    for i in text3:    
        a = text3.count(i)
        d[i] = a  #统计text2中i的频次a，并将结果导入字典
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True)
    #将字典里的元素按照value的降序排列
    print(d1)
    return

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
人之初　性本善　性相近　習相遠    苟不教　性乃遷    教之道　貴以專 
昔孟母　擇鄰處    子不學　斷機杼    竇燕山　有義方　教五子　名俱揚 
養不教　父之過　教不嚴　師之惰    子不學　非所宜　幼不學　老何為 
玉不琢　不成器　人不學　不知義    為人子　方少時　親師友　習禮儀 
    香九齡　能溫席　孝於親　所當執    融四歲　能讓梨　弟於長　宜先知 
    首孝弟　次見聞　知某數　識某文    一而十　十而百　百而千　千而萬 
    三才者　天地人　三光者　日月星    三綱者　君臣義　父子親　夫婦順 
    曰春夏　曰秋冬　此四時　運不窮    曰南北　曰西東　此四方　應乎中 
    曰水火　木金土　此五行　本乎數    曰仁義　禮智信　此五常　不容紊 
    稻粱菽　麥黍稷　此六穀　人所食    馬牛羊　雞犬豕　此六畜　人所飼 
    曰喜怒　曰哀懼　愛惡欲　七情具    匏土革　木石金　與絲竹　乃八音 
    高曾祖　父而身　身而子　子而孫    自子孫　至玄曾　乃九族　人之倫 
    父子恩　夫婦從　兄則友　弟則恭    長幼序　友與朋　君則敬　臣則忠 
    此十義　人所同  凡訓蒙　須講究    詳訓詁　名句讀  為學者　必有初 
    小學終　至四書  論語者　二十篇    群弟子　記善言  孟子者　七篇止　 
    講道德　說仁義  作中庸　子思筆　中不偏　庸不易    作大學　乃曾子 
'''

def stats_text_cn(text):
    text1 = []  #设置一个空列表用来存储中文字符
    for cn in text:     
        if '\u4e00' <= cn <= '\u9fff':  #判断text中的每个字符是否属于中文字符，是的话就加入到列表text1中，中文标点符号都去掉
            text1.append(cn)
    d = {}  #新建一个空字典保存统计结果
    for zh in text1:
        d[zh] = text1.count(zh)  #将统计text1中的字频a导入到字典d中
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True) #以字典中的频次value进行从高到低排序
    print(d1)
    return text


func = stats_text(stats_text_en(text), stats_text_cn(text))
print(func())
