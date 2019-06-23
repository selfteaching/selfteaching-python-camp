
import string
import pprint

text = '''1. 在 1001S02E06_stats_word.py 中定义⼀一个名为 stats_text_cn 的函数，函数接受⼀一 个字符串串 text 作为参数
2. 实现该函数的功能:统计参数中每个中⽂文汉字出现的次数，最后返回⼀一个按字频降序排列列的 数组
3. 为 stats_text_cn 添加注释说明'''

#参数：字符串、文本，输出按汉子的统计排名
def stats_text_cn(text):
    text = text.replace('，','')
    text = text.replace('!','')
    text = text.replace('.','')
    text = text.replace('*','')
    text = text.replace('⼀','')
    text = text.replace('?','')
    text = text.replace(':','')
    text = text.replace('_','')
    text = text.replace('\n','')

    new_list = list(text)
    #用于检测是否位数字
    num_list = ('1','2','3','4','5','6','7','8','9','0')
    int_array = []
    #用于检测是否为字母
    for i in range(65,123):
        int_array.append(i)
    dir = {}
    for item in new_list:
        item = item.strip()
        if item == '':
            continue
        if item in num_list:
            item = ''
            continue
        elif ord(item) in int_array:
            item = ''
            continue
        if item not in dir:
            dir[item] = 1
        else:
            dir[item] += 1        
    #把汉子装入词典
    dir = sorted(dir.items(),key = lambda x:x[1] ,reverse = True)
    return dir

pprint.pprint(stats_text_cn(text))