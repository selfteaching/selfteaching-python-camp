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

#该函数的功能是将带有“,.*-!?""”标点符号的英文单词字符串中的单词进行单词出现个数统计，
#最后返回一个按词频降序排列的数组
def stats_text_en(str):
    #将文档中的大小写全部换为小写
    str=str.lower()
    #将文档中的标点符号，全部换为空
    biaodian=',.*-!?"":'
    for i in biaodian:
        str=str.replace(i,'')
    #将字符串转换为单词列表
    str=str.split()
    #开始统计单词列表中单词个数
    str_dict={}
    
    for char in str:
        if char in str_dict:
            count=str_dict[char]
        else:
            count=0
        count +=1
        str_dict[char]=count
    #循环结束后，会生成一个单词及单词个数的字典，这是的字典没有排序
    #下面对字典进行排序
    char_dict=sorted(str_dict.items(),key=lambda x:x[1],reverse=True)
    
    print(char_dict)#输出排序后的字典
    
stats_text_en(text)



#该函数用于统计字符串中每个汉字出现的个数。需要输入字符串，输出的结果是按照降序排列的以中文汉字及其字频为元组的一个字典
def stats_text_cn(str):
    #移除字符串头尾的空格和换行符号
    str=str.strip()
    #去除所有的标点符号
    biaodian='。，“”…，——，？：、！《》'
    for i in biaodian:
        str=str.replace(i,'')
    #目前字符串str中应该只包含汉字，下面对汉字字符串进行统计和
    #方法与统计单词是后基本一样，因为这里是统计中文汉字个数，所以每个汉字都是一个元素，
    #于是没有必要去将字符串在转换成一个单词列表
    char_dict={}
    for char in str:
        if char in char_dict:
            count=char_dict[char]
        else:
            count=0
        count +=1
        char_dict[char]=count
    char_dict=sorted(char_dict.items(),key=lambda x:x[1],reverse=True)
    #输出最后的结果
    print(char_dict)