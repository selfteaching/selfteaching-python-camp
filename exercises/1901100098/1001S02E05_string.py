simple_text='''
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
#1.���ַ������� text ?�� better ȫ���滻�� worse

# ����str���͵� replace 
text=simple_text.replace('better','worse')
print('���ַ������� text ?�� better ȫ���滻�� worse ',text)
# 2.�������а��� ea �ĵ����޳�
# �Ƚ��ַ������� �հ��ַ� �ָ��list ,Ҫ����str���� split
words=text.split()
# ����һ��list ��������� ���˺�ĵ���Ҫ����list���͵� filter
filtered=[]
# �� for...in  ѭ��һ��words ���Ԫ�أ�Ȼ���жϵ������Ԫ���Ƿ����ea
for word in words:
    if word.find('ea')<0:
        filtered.append(word)
print('�������а��� ea �ĵ����޳�',filtered)

# 3 ���д�Сд��ת
swapcased=[i.swapcase() for i in filtered]
print('��Сд��ת',swapcased)

#5�����ʰ���A��Z��������
print('���ʰ�����������',sorted(swapcased))

