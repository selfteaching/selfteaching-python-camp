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
import re
fuhao= ",.!-*&" #去除字符串中所有除单词和汉字以外 的符号
for str in fuhao:
    text = text.replace(str,'')
print(text)
#创建一个名为stats_text_en的函数
#使用字典（dicict）统计字符串样本text中各个英文单词出现的次数

def stats_text_en(text):
    '''统计单词次数.
    
    使用字典（dict)统计text中每个英文单词出现的次数.'''
    result = re.sub("[^A-Za-z]", " ", text.strip())
    dic= {}    
    for x in result.split( ):
        if not x in dic:
            dic[x] = 1
        else:
            dic[x] = dic[x]+1
    return dic

#print(stats_text_en(text))
frequency = stats_text_en(text)
print('**********************************************')
print("按照出现次数从大到小输出所有的单词及出现的次数")
print('**********************************************')
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))

#创建一个名为stats_text_cn的函数，功能：统计每个中文汉字出现的次数
def stats_text_ch(text):
  '''统计汉字次数.
    
    使用字典（dict)统计text中每个汉字出现的次数.'''
  dictionary={}  #引用一个空字典
  for i in text:
     if u'\u4e00' <= i <= u'\u9fa5':   #提取中文汉字   \u是unincode编码，u4e00是十六进制表达值
         dictionary[i]=text.count(i)
  return dictionary
#print(stats_text_ch(text))
frequency = stats_text_ch(text)
print('**********************************************')
print("按照出现次数从大到小输出所有的汉字及出现的次数")
print('**********************************************')
print (sorted(frequency.items(), key=lambda frequency: frequency[1],reverse=True))