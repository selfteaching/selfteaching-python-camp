from collections import Counter
# ͳ�Ʋ�����ÿ��Ӣ�ĵ��ʳ��ֵĴ���
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        # �� str ���� �� isascii �����ж��Ƿ���Ӣ�ĵ���
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)


# ͳ�Ʋ�����ÿ�����ĺ��ֳ��ֵĴ���
def stats_text_cn(text,count):
    cn_characters = []
    for character in text:
        # unicode �� ���� �ַ��ķ�Χ
        if '\u4e00' <= character <= '\u9fff':
            cn_characters.append(character)
    return Counter(cn_characters).most_common(count)
        


def stats_text(text,count):
    '''
    �ϲ� Ӣ�Ĵ�Ƶ �� ������Ƶ �Ľ��
    '''
    if not isinstance(text,str):
        raise ValueError('�������ͱ������ַ�������%s'% type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)


