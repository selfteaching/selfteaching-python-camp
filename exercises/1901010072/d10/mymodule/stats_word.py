from collections import Counter
import jieba
seg_list = jieba.cut("text", cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))


#统计参数中每个中文汉字出现的次数
def stats_text_cn(text, count):
    cn_characters=[]
    for character in text:
        if '\u4e00'<=character<='\u9fff'and len(character)>=2:
            cn_characters.append(character)
    return Counter(cn_characters).most_common(20)

def stats_text(text,count):
    '''
    合并英文词频和中文词频的结果
    '''
    if not isinstance(text,str):
        raise ValueError('参数必须是str类型，输入类型%s'%type(text))
    return stats_text_cn(text,count)