# ��װͳ��Ӣ?���ʴ�Ƶ�ĺ���
def stats_text_en(text):
    elements=text.split()
    words=[]
    symbols=',.*-!'
    for element in elements:
        for symbol in symbols:
            element=element.replace(symbol,'')
        #�� str ���� �� isascii �����ж��Ƿ���Ӣ�ĵ���
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set (words) 

    for word in word_set:
        counter[word]=words.count(word)
    return sorted(counter.items(),key=lambda x :x[1],reverse=True)

#ͳ�Ʋ�����ÿ�����ĺ��ֵĳ��ִ���
def stats_text_cn(text):    
    cn_characters = []
    for character in text:
        if'\u4e00' <= character <='\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set =set(cn_characters)
    for character in cn_character_set:
        counter[character]=cn_characters.count(character)
    return sorted(counter.items(),key=lambda x :x[1],reverse=True)



def stats_text(text):
#�ϲ�Ӣ�Ĵ�Ƶ��������Ƶ�Ľ��
    return stats_text_en(text) + stats_text_cn(text)

cn_text ='''
�泯�� ��ů����
���ߣ�����

����������һ���Ҹ�����
ι��������������
�������𣬹�����ʳ���߲�
����һ�����ӣ��泯�󺣣���ů����

�������𣬺�ÿһ������ͨ��
���������ҵ��Ҹ�
���Ҹ�����������ҵ�
�ҽ�����ÿһ����

��ÿһ����ÿһ��ɽȡһ����ů������
İ���ˣ���ҲΪ��ף��
Ը����һ�����õ�ǰ��
Ը���������ճɾ���
Ը���ڳ�������Ҹ�
��ֻԸ�泯�󺣣���ů����
'''
en_text='''
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
cn_text='''
�泯�� ��ů����
���ߣ�����

����������һ���Ҹ�����
ι��������������
�������𣬹�����ʳ���߲�
����һ�����ӣ��泯�󺣣���ů����

�������𣬺�ÿһ������ͨ��
���������ҵ��Ҹ�
���Ҹ�����������ҵ�
�ҽ�����ÿһ����

��ÿһ����ÿһ��ɽȡһ����ů������
İ���ˣ���ҲΪ��ף��
Ը����һ�����õ�ǰ��
Ը���������ճɾ���
Ը���ڳ�������Ҹ�
��ֻԸ�泯�󺣣���ů����
'''
#����_name_==_main_
#һ����������ļ��� ���� �����ʱ�����������ʽ����
if __name__ == "__main__":
    en_result=stats_text_en(en_text)
    cn_result=stats_text_cn(cn_text)
    print('ͳ�Ʋ�����ÿ��Ӣ�ĵ��ʳ��ֵĴ���==>\n',en_result)
    print('ͳ�Ʋ�����ÿ�����ĺ��ֳ��ֵĴ���==>\n',cn_result)