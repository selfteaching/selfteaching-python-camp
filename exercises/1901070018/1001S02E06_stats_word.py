text = '''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
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
china ='''Unicode只有一个字符集，
中、日、韩的三种文字占用了Unicode中0x3000到0x9FFF的部分  
Unicode目前普遍采用的是UCS-2,它用两个字节来编码一个字符, 
比如汉字"经"的编码是0x7ECF,注意字符编码一般用十六进制来 表示,
为了与十进制区分,十六进制以0x开头,0x7ECF转换成十进制 就是32463,
UCS-2用两个字节来编码字符,两个字节就是16位二进制, 2的16次方等于65536,
所以UCS-2最多能编码65536个字符。 编码从0到127的字符与ASCII编码的字符一样,
比如字母"a"的Unicode 编码是0x0061,十进制是97,
而"a"的ASCII编码是0x61,十进制也是97, 对于汉字的编码,
事实上Unicode对汉字支持不怎么好,这也是没办法的, 
简体和繁体总共有六七万个汉字,而UCS-2最多能表示65536个,
才六万 多个,所以Unicode只能排除一些几乎不用的汉字,
好在常用的简体汉字 也不过七千多个,为了能表示所有汉字,Unicode也有UCS-4规范,
就是用 4个字节来编码字符,不过现在普遍采用的还是UCS-2，只用两个字节来 编码,
看一下Unicode对汉字的编码'''

def stats_text_en(text):
    '''统计英文参数中的词频并且并且降序排列'''
    char = ',.-:;!@#$%^&*()-+=<>?/\\`~|[]{}，。？、·~！@#￥%……&*（）——+-={}【】、|；：“”‘’'
    for i in char:
        text = text.replace(i, '')
    list1 = text.split()
    dic = {}

    for i in list1:
        num = list1.count(i)
        dic[i] = num
    list2 = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    return list2


def stats_text_cn(text):
    '''统计中文参数中的词频并且并且降序排列'''
    list1 = []
    dic = {}
    for i in text:
        if '\u4e00' <= i <= '\u9fff':
            list1.append(i)
            dic[i] = list1.count(i)
    list2 = sorted(dic.items(), key=lambda d: d[1], reverse=True)
    return list2


print(stats_text_en(text))
print(stats_text_cn(china))

