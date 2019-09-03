import stats_word

#text = 'abc123你是谁'
text = 2345

if __name__ == '__main__':
    print('合并统计中英文频次')
    try:
        list1 = stats_word.stats_text(text)
        print(list1)
    except ValueError:
        print('请传入正确的字符串给stats_text()函数！')