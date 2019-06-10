#作业. 将统计中⽂文词频和英⽂文词频的函数封装为⼀一个模块
#解决问题思路：首先将文档分为英文和中文两个文档保存在本地文档，然后在建立一个新函数分别调用之前的stats_text_en(s)、stats_text_cn(S)
#函数
Text = open('D:\\dayfive\ygysyw.txt')
s = Text.read()
#之前复制文档在代码的做法有偷懒的想法，如果碰到文档很长的话难道我要全文复制？，要创建文件然后在读取:
def stats_text_en(s):  #定义一个函数stats_text_en
    counts = dict()   #新建一个空字典
    words = s.split()  #使用split方法把text字符串中的每个单词分割，且返回的是一个列表  

    for word in words:   #使用一个for循环
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for key, value in sorted(counts.items(), key=lambda item: item[1], reverse = True):#山寨来的
        print("%s: %s" % (key, value), end=" ")
        



text = open('D:\\dayfive\ygyszw.txt')
S = text.read()
import jieba

def stats_text_cn(S):  #定义一个函数stats_text_en
    counts = dict()   #新建一个空字典
    words = " ".join(jieba.cut(S))  #使用split方法把text字符串中的每个单词分割，且返回的是一个列表  #前一句话是之前的理解，可是通过百度（这里我
    #没有google，因为我感觉搜索如何中文汉字分词，百度应该是更好的方法）我理解了英文单词之间是有强制的空格可是中文汉字之间却没有强制的空格，搜索
    #之后再玉树芝兰这个公众号里搜到了“结巴分词”感觉不错，这一句就是山寨模仿出来的，但是我不嫌初期的自己笨拙，因为每个人都要从笨拙开始，什么时候都不晚

    for word in words:   #使用一个for循环
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    for key, value in sorted(counts.items(), key=lambda item: item[1], reverse=True):
        print("%s: %s" % (key, value), end=" ")
        


def stats_text():  
    stats_text_en(s)
    stats_text_cn(S)

