template = '''
The Zen of Python, by Tim Peters
美丽 is better than 丑陋.
清楚 is better than 含糊.
简单 is better than 复杂.
复杂 is better than 难懂.
单一 is better than 嵌套.
稀疏 is better than 稠密.
可读性计数.
Special cases aren't special enough to 打破规则.
即使练习会使得不再纯粹.
但错误不应该用沉默来掩盖.
Unless explicitly silenced.
面对起义，拒绝猜的诱惑.
有且只有一个办法.
Although that way may not be obvious at first unless you're Dutch.
尝试总比从未试过要强.
Although never is often better than *right* now.
如果执行很难被解释，那将是一个很糟的想法.
如果执行很容易解释，这会是一个好点子.
Namespaces are one honking great idea -- 让我们继续为之努力!
'''


#判断是否包含英文
def stats_text_en(text):
    endic = {}
    for ch in text:
        if u'a' <= ch <= u'z' or u'A' <= ch <= u'Z':
            endic[ch] = text.count(ch)
    return endic


#定义检索中文函数
def stats_text_en(text):
    cndic = {}
    for i in text:
        if u'\u4e00' <= i <= u'\u9fff':
            cndic[i] = text.count(i)
    return cndic

def main():
    cndic = stats_text_en(template) #调用检索中文频次函数

    cndic = sorted(cndic.items(),key=lambda item:item[1],reverse = True)  #对字典进行按值大小从大到小排序
    print(cndic) 

    endic =stats_text_en(template) #调用检索中文频次函数

    endic = sorted(endic.items(),key=lambda item:item[1],reverse = True)
    print(endic)


if __name__ == '__main__':
    main()


