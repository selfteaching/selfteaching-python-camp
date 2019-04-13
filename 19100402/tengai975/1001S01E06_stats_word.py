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
Although that han never.
Although never is often better than *right* now.
If the implementatway may not be obvious at first unless you're Dutch. 
Now is better tion is hard to explain, it's a bad idea.
 If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!

美丽总比丑陋好。
显式比隐式好。
简单总比复杂好。
复杂总比复杂好。
平的比嵌套的好。
稀疏总比密集好。
可读性。
特殊情况还不足以打破规则。
虽然实用性胜过纯洁性。
错误不应该悄无声息地过去。
除非显式地沉默。
面对敏锐，拒绝猜测的诱惑。
应该有一种——而且最好只有一种--显而易见的方法来做到这一点。
不过，除非你是荷兰人，否则这种方式一开始可能并不明显。
现在总比不做好。
虽然从来没有比“现在”更好。
如果实现很难解释，这是一个坏主意。
如果实现很容易解释，这可能是一个好主意。
名称空间是一个很棒的主意--让我们做更多这样的事情!
''' 

#定义一个名为stats_text_en的函数，函数接受一个字符text作为参数，使用字典统计参数
#中每个英文单词出现的次数，最后返回一个按词频降序排列的数组   
#使用字典（dict）统计字符串样本text中各个英文单词出现的次数

def stats_text_en(str): #该函数的功能是是把带有各种英文标点符号的英文单词字符串中的单词进行单词个数统计
    str=str.lower()  #将所有单词变成小写
    biaodian=',.*-!?:，。“”'  #使字符串text里的标点符号，全部换成空格
    for i in biaodian:
        str=str.replace(i,'') 
    str=str.split() #把字符串转换成单词列表  
    str_dict={}   #统计列表中单词个数

    for char in str:
        if char in str_dict:
            count=str_dict[char]
        else:
            count=0
        count +=1
        str_dict[char]=count
#循环结束后会生成一个单词及个数的字典
#对字典进行降序
    char_dict=sorted(str_dict.items(),key=lambda x:x[1],reverse=True)


                
    print(char_dict)#输出结果

stats_text_en(text)



#该函数用于统计字符串中每个汉字出现的次数，最后返回一个按字频排列的数组
#之前那个函数已经包含了中文的，我现在还没有思路把两个中英文的字典一起排序
#那么基本的部分一样，汉字不用转换成单词列表，可以直接排
def stats_text_en(str): #引入一个函数定义
    str=str.split()   #用空格进行切片
    biaodian='。，“”？！-' #移除空格号和换行符号还有标点符号
    for i in biaodian:
        str=str.replace(i,'')
    char_dict={}#建立一个字典
    for char in str:  #循环统计中文字符并降序
        if char in char_dict:
            count=char_dict[char]
        else:count=0
        count=+1
        char_dict[char]=count 
    char_dict=sorted(char_dict.items(),key=lambda x:x[1],reverse=True)
    print(char_dict)#输出结果






