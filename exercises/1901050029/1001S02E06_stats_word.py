# Filename : 1001S02E06_stats_word.py
# author by : �Ž���

from collections import Counter
import re

text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
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
�����׺���Ϊˮ����ȴ��ɽ�����ơ�Ϫ�Ƴ����ճ���,ɽ����������¥
'''

#���庯������ȥ��Ӣ���ı��е������ַ���!"#$%&()*+,-./;:<=>?@[\\]^��_{|}~��������
def getText(text):
    txt = text
    txt = txt.lower()
    result = re.sub("[^A-Za-z]", " ", txt.strip())
    for ch in '!"#$%&()*+,-./;:<=>?@[\\]^��_{|}~':
        result = result.replace(ch, " ")
    return result

#���庯������ͳ��Ӣ�ĵ��ʴ�Ƶ��������Ƶ������� 
def stats_text_en(text):
    hamletTxt = getText(text)
    words = hamletTxt.split()
    word = Counter(words)
   
    print('Ӣ�ĵ��ʴ�Ƶͳ�ƽ����','\n', word)    
    

#���庯������ͳ�����ĺ�����Ƶ��������Ƶ�������
def stats_text_cn(text):
    result = re.findall(u'[\u4e00-\u9fff]+', text)    #���ֵ�unicode��Χ
    words = ''.join(result)
    word = Counter(words)
   
    print('���ִ�Ƶͳ�ƽ����','\n', word)   
    
####����������
#import collections
#import re

#def stats_text_en(text):
    
    #result = re.sub("[^A-Za-z]", " ", text.strip())
    #newList = result.split()
    #print('Ӣ�ĵ��ʴ�Ƶͳ�ƽ���� ',collections.Counter(newList),'\n')

#def stats_text_cn(text):
    #result1 = re.findall(u'[\u4e00-\u9fff]+', text)
    #newString = ''.join(result1)
    #print('���ִ�Ƶͳ�ƽ���� ', collections.Counter(newString), '\n')
    
#stats_text_en(text)
#stats_text_cn(text)