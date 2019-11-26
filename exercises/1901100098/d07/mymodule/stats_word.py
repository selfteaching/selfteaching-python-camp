# 封装统计英?单词词频的函数
def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        #用 str 类型 的 isascii 方法判断是否是英文单词
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set (words) 

    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x :x[1],reverse=True)

#统计参数中每个中文汉字的出现次数
def stats_text_cn(text):    
    cn_characters = []
    for character in text:
        if'\u4e00' <= character <='\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set =set(cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x :x[1],reverse=True)



def stats_text(text):
#合并英文词频和中文字频的结果
    return stats_text_en(text) + stats_text_cn(text)

cn_text ='''
面朝大海 春暖花开
作者：海子

从明天起，做一个幸福的人
喂马，劈柴，周游世界
从明天起，关心粮食和蔬菜
我有一所房子，面朝大海，春暖花开

从明天起，和每一个亲人通信
告诉他们我的幸福
那幸福的闪电告诉我的
我将告诉每一个人

给每一条河每一座山取一个温暖的名字
陌生人，我也为你祝福
愿你有一个灿烂的前程
愿你有情人终成眷属
愿你在尘世获得幸福
我只愿面朝大海，春暖花开
'''
en_text='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
cn_text='''
面朝大海 春暖花开
作者：海子

从明天起，做一个幸福的人
喂马，劈柴，周游世界
从明天起，关心粮食和蔬菜
我有一所房子，面朝大海，春暖花开

从明天起，和每一个亲人通信
告诉他们我的幸福
那幸福的闪电告诉我的
我将告诉每一个人

给每一条河每一座山取一个温暖的名字
陌生人，我也为你祝福
愿你有一个灿烂的前程
愿你有情人终成眷属
愿你在尘世获得幸福
我只愿面朝大海，春暖花开
'''
#搜索_name_==_main_
#一般情况下在文件内 测试 代码的时候以下面的形式进行
if __name__ == "__main__":
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print('统计参数中每个英文单词出现的次数==>\n',en_result)
    print('统计参数中每个中文汉字出现的次数==>\n',cn_result)