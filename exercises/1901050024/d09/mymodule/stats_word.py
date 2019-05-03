import collections
import re
import jieba
def stats_text_en(en,count1):
    ''' 1. 英文词频统计：使用正则表达式过滤英文字符，使用Counter统计并排序。
        2. 参数类型检查，不为字符串抛出异常。
    '''
    if type(en) == str : 
        text_en = re.sub("[^A-Za-z]", " ", en.strip())
        enList = text_en.split( )
        count1 = int(input('请输入获取的英文单词数量：'))
        return collections.Counter(enList).most_common(count1)
    else: 
        raise ValueError ('type of argumengt is not str')

def stats_text_cn(cn,count2):
    ''' 1. 使用jieba第三方库精确模式分词。
        2. 使用正则表达式过滤汉字字符。
        3. 使用for循环判断分词后词频列表元素长度大于等于2的生成新列表。
        4. 使用标准库collections.Counter()统计词频并限制统计数量。 
        5. 参数类型检查，不为字符串抛出异常。
    '''
    if type(cn) == str : 
        cnList = re.findall(u'[\u4e00-\u9fff]+', cn.strip())
        cnString = ''.join(cnList)
        segList = jieba.cut(cnString,cut_all=False)
        cnnewList = []
        for i in segList :
            if len(i) >= 2 :
                cnnewList.append(i)
            else:
                pass                
        count2 = int(input('请输入获取的中文单词数量：'))    
        countList = collections.Counter(cnnewList).most_common(count2)
        return countList
    else:
        raise ValueError ('type of argumengt is not str')

def stats_text(text_en_cn,count_en_cn) :
    ''' 1. 合并英汉词频统计：调用stats_text_en()和stats_text_cn()并合并其结果。
        2. 参数类型检查，不为字符串抛出异常。
    '''
    try:
        return (stats_text_en(text_en_cn,count_en_cn)+stats_text_cn(text_en_cn,count_en_cn))
    except ValueError as a:
        print(a)