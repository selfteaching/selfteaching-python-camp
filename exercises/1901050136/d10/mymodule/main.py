# this script is to install and use the Other Library
import stats_word as s
import jieba

if __name__ == "__main__":
    # statistics for the chinese words in the file('tang300.json')

    file_path = '/Users/tsuishihhao/Documents/GitHub/selfteaching-python-camp/exercises/1901050136/d09/mymodule/tang300.json' # absolute address 
    with open(file_path,'r',encoding='utf-8') as f:
        text = f.read() # original text

        # delete the non-chinese character
        characters_cn = ''
        for character in text:
            if '\u4e00'<= character <= '\u9fff':
                characters_cn += character
        text = characters_cn # new text without non-chinese chars

        # dividing words using jieba
        words = jieba.cut(text)
        text = (' '.join(words))

        # select the words whose length >= 2
        text_list = text.split()
        text_2 = '' # this str object store all the words larger 2
        # print('text_list',text_list)
        for chars in text_list:
            if len(chars) >= 2:
                chars = ' ' + chars
                text_2 += chars
        # print('text_2',text_2)
        text = text_2 # store all the words larger 2

        try:
            print('the sorted word frequencies for the input text of tang300: \n{} '.
                format(s.stats_text_en(text)[0].most_common(20))) # using stats_word_en since statstics for words not for every single Han Chars
        except Exception as e:
            print(e)