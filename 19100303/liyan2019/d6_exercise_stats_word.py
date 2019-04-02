# 定义一个函数，以text作为参数，统计text中英文单词频次并返回按词频降序排列的数组

def stats_text_en(text):
    """count english words in the text"""
import d5_exercise_stats_text



def stats_text_cn(text):
    """count chinese words in text"""
    wordcount={}
    for i in text:
        if  u'\u4e00' <= i <= u'\u9fff':
            wordcount[i]=text.count(i)
    wordcount=sorted(wordcount.items(),key=lambda x:x[1],reverse=True)
    return wordcount

text='''
python作业完成作业作业'''
print(stats_text_cn(text))

text='''
python is interesting and learning is iinteresting too.'''
print(stats_text_en(text))
    ###如何查看函数执行结果呢？？