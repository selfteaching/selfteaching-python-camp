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

def stats_text_en(text):
    dict = {}
    import re
    ''' 保留英文单字 '''
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    list = re.findall(en_pattern, template)
    
    #print(list)
    for i in list:
        ''' 统计次数 '''
        num = list.count(i)
        '''使用setdefault给list中的词按次序添加键，并设定值为num'''
        dict.setdefault(i,num)
        '''按照每个词的num作为key值排序'''
        tup1 = sorted(dict.items(),key = lambda items:items[1],reverse = True)

    dict2 = {}

    '''遍历tup1'''
    for i in tup1:
        dict2[i[0]] = dict[i[0]]
    return dict2


def stats_text_cn(text):
    dict = {}
    import re
    ''' 保留中文单字 '''
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    list = re.findall(cn_pattern, template)
    
    #print(list)
    for i in list:
        num = list.count(i)
        dict.setdefault(i,num)
        tup1 = sorted(dict.items(),key = lambda items:items[1],reverse = True)

    dict2 = {}

    '''遍历tup1'''
    for i in tup1:
        dict2[i[0]] = dict[i[0]]
    return dict2



def main():
    stats_text_en(template)
    stats_text_cn(template)


if __name__ == '__main__':
    main()