from collections import Counter
import jieba

# pip install -i https://pypi.tuna.tsinghua.edu.cn/simple jieba

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
    words = jieba.cut(text)
    tmp = []
    for i in words:
        if len(i) > 1:
            tmp.append(i)
    return Counter(tmp).most_common(count)
        


def stats_text(text,count):
    '''
    �ϲ� Ӣ�Ĵ�Ƶ �� ������Ƶ �Ľ��
    '''
    if not isinstance(text,str):
        raise ValueError('�������ͱ������ַ�������%s'% type(text))
    return stats_text_en(text,count) + stats_text_cn(text,count)


# ���� __name__ == '__main__'
# һ����������ļ��� ���� �����ʱ�����������ʽ����
# if __name__ == '__main__':

