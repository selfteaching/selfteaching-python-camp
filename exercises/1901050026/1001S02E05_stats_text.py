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

# ʹ�á��ֵ䡱ͳ�������ı��г��ֵĵ��ʴ���
# ������һ���Ľ���Ӵ�С���

t = t.replace(',',' ').replace('.',' ').replace('--',' ').replace('*',' ').replace('!',' ') # ȥ���

t = t.lower() # ȫ������Сд
t = t.split() # ����ַ���
d = {} # ���ֵ�
for i in t:
    count = t.count(i) # ����
    r1 = {i:count} # ������ǰ����Ƶ�ں�
    d.update(r1) #�ϴ�r1��d��ȥ
print(d)

print('\n���ճ��ִ�����С������е���\n')
d = sorted(d.items(),key=lambda x:x[1],reverse=True)
# sorted(iterable,*,key=None,reverse=False) lambda�Ǹ�����Ķ��庯���������ǵĶ���ı�����ʽ�������Ժ��о���reverse=True�ǵߵ�����˼
print(d)
