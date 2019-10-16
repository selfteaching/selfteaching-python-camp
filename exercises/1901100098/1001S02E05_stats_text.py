# ͳ���ַ�����Ӣ�ĵ��ʳ��ֵĴ���
sample_text='''
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
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
elements=sample_text.split()
words=[]
#�ȸ����б�ѡ����Ҫ�޳��ķǵ��ʷ���
symbols=',.*-!'
for element in elements:
#����һ��Ҫ�޳��ķ���
    for symbol in symbols:
 #����滻�ַ��ţ���''�滻�ַ���ռλ��      
        element=element.replace(symbol,'')
#�޳������element�ĳ��Ȳ�Ϊ0������������
    if len(element):
       words.append(element)
print('������Ӣ�ĵ���==>',words)

#��ʼ��һ�� dict ���ֵ䣩���͵ı�����������ŵ��ʵĴ���

counter = {}
# set(��������) ����ȥ���б�����ظ�Ԫ�أ�������for...in�����ѭ������
word_set = set (words) 
for word in word_set:
        counter[word]=words.count(word)
print('Ӣ�ĵ��ʳ��ִ���==>',counter)

# 2.���յ��ʳ��ִ����Ӵ�С������е��ʼ����ִ���
# ���ú��� sorted �Ĳ���key ��ʾ���պ�������һ��ֵ��������
# dict ���͵�counter�� items���� �᷵��һ��������Ӧ�key,value����Ԫ���б�  ����ʵ����key�����ʣ�value ���������
print('�Ӵ�С������е��ʼ����ִ���==>',sorted(counter.items(),key=lambda x :x[1],reverse=True))
