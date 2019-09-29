#stats_text_en 封装统计英文单词词频的函数
def stats_text_en(text):
    if isinstance(text,str) is False:
        print('您输入的内容不是字符串类型！')
        raise ValueError
    else:
        pass
    a=text.split()
    x=[]
    for i in a:
        if i.isalpha() is True:
            x.append(i)
    from collections import Counter
    n=int(input('请输入您需要的词频最高的前n个词的具体数值：'))
    return dict(Counter(x).most_common(n))

#stats_text_cn 封装统计中文汉字字频的函数
import jieba
def stats_text_cn(text):
    if isinstance(text,str) is False:
        print('您输入的内容不是字符串类型！')
        raise ValueError
    seg_list=jieba.lcut(text)
    x=[]
    for i in seg_list:
        if '\u4e00'<=i<='\u9fa5' and len(i)>=2:
            x.append(i)
    from collections import Counter
    return dict(Counter(x).most_common(20))

#stats_text 分别调用stats_text_en , stats_text_cn ，输出合并词频统计结果
def stats_text(text):
    if isinstance(text,str) is False:
        print('您输入的内容不是字符串类型！')
        raise ValueError
    new_dic=dict(stats_text_en(text),**stats_text_cn(text))
    return new_dic

if __name__=='__main__':
#通过网络请求获得网页内容，使⽤分词工具对中文字符串进行分词，统计词频，得出结果，发送给到指定的邮箱
    import getpass
    sender=input('请输入发件人邮箱：')
    password=getpass.getpass('输入发件人邮箱密码(可复制粘贴):')
    recipient=input('请输入收件人邮箱：')

    import requests
    response=requests.get('https://mp.weixin.qq.com/s/pLmuGoc4bZrMNl7MSoWgiA')
    from pyquery import PyQuery
    document=PyQuery(response.text)
    content=document('#js_content').text()
    body=str(stats_text_cn(content))

    import yagmail
    yag=yagmail.SMTP(sender,password,'smtp.126.com')
    yag.send(recipient,'1901100283 自学训练营学习19群 Day11 PerryZ10',body)