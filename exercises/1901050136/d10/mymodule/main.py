# this script is to install and use the Other Library
import stats_word as s

if __name__ == "__main__":
    # statistics for the chinese words in the file('tang300.json')

    file_path = '/Users/tsuishihhao/Documents/GitHub/selfteaching-python-camp/exercises/1901050136/d09/mymodule/tang300.json' # absolute address 
    with open(file_path,'r',encoding='utf-8') as f:
        text = f.read() # original text

        try:
            print('the sorted word frequencies for the input text of tang300: \n{} '.
                format(s.stats_text_cn(text)[0].most_common(20))) # using stats_word_en since statstics for words not for every single Han Chars
        except Exception as e:
            print(e)