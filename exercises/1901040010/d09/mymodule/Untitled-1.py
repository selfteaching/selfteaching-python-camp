text = '''
This is a wonderful day. It is a sunny hot day.
昨天下雨了，今天又下雨了，明天还会下雨吗？
'''


from collections import Counter
#统计参数中每个英文单位出现的次数
def stats_text_en(text,count):
    elements = text.split()
    words = []
    symbols = ',.*-!'
    for element in elements:
        for symbol in symbols:
            element = element.replace(symbol, '')
        if len(element) and element.isascii():
            words.append(element)
    return Counter(words).most_common(count)
