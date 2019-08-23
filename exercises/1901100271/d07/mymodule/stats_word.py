def stats_text_en(en_text):  
    #此函数的功能是统计参数中的英文单词的频次，并且按照词频从高到低排序输出
    en_text = en_text.split()
    text1 = []       
    symbols = ",.!*-"
    for en in en_text:
        for symbol in symbols:
            en = en.replace(symbol, "")
        if len(en):
            text1.append(en)
    d = {}   
    for i in text1:    
        a = text1.count(i)
        d[i] = a  
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True)
    return d1


def stats_text_cn(cn_text):
    #此函数的功能是统计参数中的中文单词的频次，并且按照词频从高到低排序输出
    text1 = []  
    for cn in cn_text:     
        if '\u4e00' <= cn <= '\u9fa5':  
            text1.append(cn)
    d = {}  
    for zh in text1:
        d[zh] = text1.count(zh)  
    d1 = sorted(d.items(), key = lambda item : item[1], reverse = True) 
    return d1

if __name__ == "__main__":
    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print("统计参数中每个英文单词的频次: \n", en_result)
    print("统计参数中每个中文单词的频次: \n", cn_result)

def stats_text(text):
    return stats_text_en(en_text) + stats_text_cn(cn_text)

en_text = '''
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
cn_text = '''
人之初　性本善　性相近　習相遠    苟不教　性乃遷  教之道　貴以專 
昔孟母　擇鄰處  子不學　斷機杼    竇燕山　有義方　教五子　名俱揚 
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