text = '''
Alice was beginning to get very bored.She and her sister were sitting under the trees.
Her sisterwas reading,but Alice had nothing to do.Once or twice she looked into her sister's book,
but ithad no pictures or conversations in it.

爱丽丝开始觉得有点无聊了。她和姐姐正坐在树下。姐姐在看书，而爱丽丝无事可做。
她不时看看姐姐的书，里面既没有图画，也没有对话。

And what is the use of a book,"thought Alice,"without pictures or conversations?
一本书没有图画和对话有什么用呢？爱丽丝想。

She tried to think of something to do,but it was a hot day and she felt very sleepy andstupid.
She was still sitting and thinking when suddenly a White Rabbit with pink eyes ran pasther.

她想找点什么事儿做做，可天气很热，她觉得又因又无聊。正坐在那儿想事，忽然，一只长着粉红眼睛的白兔跑过她身边。

There was nothing really strange about seeing a rabbit.
And Alice was not very surprised whenthe Rabbit said,Oh dear!Oh dear!I shall be late!
Perhaps it was a little strange, Alice thoughtlater,but at the time she was not surprised.

看到一只兔子真没有什么可奇怪的。兔子说话时爱丽丝居然也不觉得太奇怪。兔子说，噢，天哪！噢，天哪！我要迟到了！
后来爱丽丝想起这事觉得有点儿奇怪，但当时她并不觉得有什么奇怪。
'''
#去除text里的标点符号
s = ",.!-*"                 #将,.!-*赋值为变量s
text = text.replace(s,'')   #调用函数replace()将字符串text中的,.!-*替换为空格后生成新变量text              

#创建一个名为stats_text_en的函数
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数
import re    #re模块提供正则表达式的匹配操作
def stats_text_en(text):  #定义函数 stats_text_en()，接收参数text
    if type(text) != str:
        raise ValueError ("This is not an str type")
    result = re.sub("[^A-Za-z]", " ", text.strip())
    d = {}
    for x in result.split( ):
        if not x in d:
            d[x] = 1
        else:
            d[x] = d[x]+1
    return d

#print(stats_text_en(text))
frequency = stats_text_en(text)
#print("按照出现次数从大到小输出所有的单词及出现的次数")
#print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))

#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
import re  #re模块提供各种正则表达式的匹配操作
def stats_text_cn(text):
    '''统计每个中文汉字出现的次数'''
    if type(text) != str:
        raise ValueError ("This is not an str type")
    result = re.findall(u'[\u4e00-\u9fff]+', text)#\u是unincode编码，u4e00是十六进制表达值
    rep = ''.join(result)
    resoult = {}
    for i in rep:
        resoult[i] = rep.count(i)
    return resoult
stats_text_cn(text = "")
#print(stats_text_cn(text))
frequency = stats_text_cn(text)
#print("按照字频降序排列")
#print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))

def stats_text(text):
    dictxxx = {}
    try:
        dictxxx = dict(stats_text_en(text),**stats_text_cn(text))
    except ValueError:
        print("stats_text(ValueError):please input string")
    except TypeError:
        print("stats_text(TypeError):please input string")
    return dictxxx

def main():
    mdict={}
    mdict=stats_text(text)
    print(mdict)

if __name__=='__main__':
    main()
