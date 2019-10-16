t = '''
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
'''

# ��ҵҪ��
# 1.��'better'ȫ���滻��'worse'���
# 2.����һ���Ľ���ｫ������ea���ĵ���ɾ��
# 3.�ӵ�2���Ľ���н����ʵĴ�Сд��ת
# 4.�ӵ�3���Ľ���н����е��ʰ�'a~z'��������

t = t.replace('better','worse') #.replace(olde,new[,count]),count�����1�Ļ���ô��ֻ�е�һ���ᱻ�滻�������Ļ�ȫ�滻
print(t)

t = t.swapcase() # ����滻��Сд,��һ��������ǰ����Ȼ�Ļ��ᱨ��
print(t)

t = t.replace(',',' ').replace('.',' ').replace('!',' ').replace('*',' ').replace('--',' ') # ȥ��������
t = t.split() # ��ֳ��ַ���
x = 'EA' #��Ϊǰһ���Ѿ���Сд�滻�ɴ�д��
y = [] #[]�б�
for i in t:
    if i.find(x)<0: # ������ʲ���EA����-1��������ֵС��0
        y.append(i) # ��ʣ��ĵ��ʼ���y
print(y)

print('\n') # �����пո�
y.sort() #����
print(y)