from wxpy import *
import d11_training1
import requests
import collections
import pyquery
from pyquery import PyQuery
import collections
from os import path
import json
import re
'''导入jieba'''
import jieba

bot = Bot()

my_friend = bot.friends().search('嘻嘻')[0]
my_friend.send('Hello WeChat!')


def stats_text_en(text):
    #dict1 = {}
    import re
    ''' 保留英文单字 '''
    en_pattern = re.compile(r'[a-zA-Z]+[\'\-]?[a-zA-Z]+')
    list1 = re.findall(en_pattern, text)
    
    return list1

def stats_text_cn(text):
    #dict1 = {}
    ''' 保留中文单字 '''
    cn_pattern = re.compile(r'[\u4e00-\u9fa5]')
    return "".join(re.findall(cn_pattern, text))
    
    '''调用collections的Counter函数'''
    #cnt = collections.Counter()
    #for word in list1:
        #cnt[word] += 1

def cut_cnwords(text):
    list2=[]
    #non_word_char = '＂＃＄％＆＇（）＊＋，－／：；＜＝＞＠［＼］＾＿｀｛｜｝～｟｠｢｣､、〃》「」『』【】〔〕〖〗〘〙〚〛〜〝〞〟〰〾〿–—‘’‛“”„‟…‧﹏'
    #non_word_char += string.punctuation + string.whitespace
    #trans = str.maketrans({key: None for key in non_word_char})
    #text = text.translate(trans)
    seg_list = jieba.cut(text, cut_all=True)

    for i in seg_list:
        if len(i)>=2:
            list2.append(i)
    return list2

def stats_text(text):
    '''使用isinstance函数验证输入的参数类型是否为str'''
    if isinstance(text, str) != True: 
        '''用raise语句来引发异常'''
        raise ValueError
    else: 
        return stats_text_en(text),stats_text_cn(text)

def main(text):
    '''提取所有英文单字'''
    enwords = stats_text_en(text)
    '''提取所有中文单字'''
    cnwords = stats_text_cn(text)
    '''分词'''
    cutcnwords = cut_cnwords(cnwords)
    return enwords+cutcnwords

@bot.register(msg_types=SHARING)#监听好友分享的消息
def auto_reply(msg):
    print(msg)
    if msg.type == "Sharing":
 
        url = msg.url
        
        '''使用requests的get获取网址全部内容'''
        response = requests.get(url)
        '''使用pyquery提取网址正文内容'''
        document = pyquery.PyQuery(response.text)
        content = document('#js_content').text()
        words = main(content)
        #print(words)

        top100 = collections.Counter(words).most_common(100)
        str100 = ','.join([str(x) for x in top100])

        print(str100)
        my_friend.send(str100)

embed()
