import re
template = '''The Zen of Python, by Tim Peters
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

#英文统计
def stats_text_en(text):

    result = {}
     #替换特殊字符
    for sb in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|}':
        text.replace(sb, ' ')
    text = text.replace(' ',',')
    text = text.strip(',').split(',')
    textList = list(text)
 
    for i in text:
        result[i]=textList.count(i)
    print(result)
    return result

#中文统计
def stats_text_cn(text):
    result = {}
     #替换特殊字符
    for sb in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|};':
        text.replace(sb, ' ')
    text = re.sub('[a-z,A-Z,\n,!]','',text)

    textList = list(text)

    for i in text:
        if(i != ' '):
             result[i]=textList.count(i)
    print(result)
    return result

def main():
    #stats_text_en(template)
    stats_text_cn(template)


if __name__ == '__main__':
    main()