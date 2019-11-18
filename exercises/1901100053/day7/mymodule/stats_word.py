# ͳ�Ʋ�����ÿ��Ӣ�ĵ��ʳ��ֵĴ���
def stats_text_en(text):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        # �� str ���� �� isascii �����ж��Ƿ���Ӣ�ĵ���
        if len(element) and element.isascii():
            words.append(element)
    counter = {}
    word_set = set(words)

    for word in word_set:
        counter[word] = words.count(word)
    # ��������ֵ�� return ���з��أ����û�� return ����ֵ��Ϊ None
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


# ͳ�Ʋ�����ÿ�����ĺ��ֳ��ֵĴ���
def stats_text_cn(text):
    cn_characters = []
    for character in text:
        # unicode �� ���� �ַ��ķ�Χ
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    counter = {}
    cn_character_set = set(cn_characters)
    for character in cn_character_set:
        counter[character] = cn_characters.count(character)
    return sorted(counter.items(), key=lambda x: x[1], reverse=True)


def stats_text(text):
    '''
    �ϲ� Ӣ�Ĵ�Ƶ �� ������Ƶ �Ľ��
    '''
    return stats_text_en(text) + stats_text_cn(text)


# ���� __name__ == '__main__'
# һ����������ļ��� ���� �����ʱ�����������ʽ����
if __name__ == '__main__':
    en_text = '''
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

    cn_text = '''
Python֮�� by Tim Peters

����ʤ�ڳ�ª
����ʤ�ڻ�ɬ
���ʤ�ڸ���
����ʤ������
��ƽʤ��Ƕ��
���ʤ�ڽ���
�ɶ��Ժ���Ҫ
����ٽ�������ʵ����֮����Ҳ����Υ����Щ����
��Ҫ�������д��󣬳�����ȷ����Ҫ������
�����ڶ��ֿ��ܣ���Ҫ����ȥ�²�
���Ǿ�����һ�֣������Ψһһ�����ԵĽ������
��Ȼ�Ⲣ�����ף���Ϊ�㲻�� Python ֮��
��Ҳ��ù�������������˼���Ͷ��ֻ����粻��
������
'''

    en_result = stats_text_en(en_text)
    cn_result = stats_text_cn(cn_text)
    print('ͳ�Ʋ�����ÿ��Ӣ�ĵ��ʳ��ֵĴ��� ==>\n', en_result)
    print('ͳ�Ʋ�����ÿ�����ĺ��ֳ��ֵĴ��� ==>\n', cn_result)
