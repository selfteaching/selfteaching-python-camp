import collections

# this script is to learn standard Library

# 1 for english word
def stats_text_en(text):
    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    text = text.strip().split()
    words = [] # for store the text after processing
    symbols = '、??:「」，。.!,“”' ''
    for word in text:
        for  symbol in symbols:
            word = word.replace(symbol,'') # delet the redundant symbols in the text
        words.append(word)

    # the collections is used in stead of set and dictionary
    cnt = collections.Counter()
    for word in words:
        if len(word):
            cnt[word] += 1
    Result = cnt
    count = len(Result)

    return Result, count


# 2 for chinese word
def stats_text_cn(text):
    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    characters_cn = [] # for storing the text after processing

    for character in text:
        if '\u4e00'<= character <= '\u9fff':
            characters_cn.append(character)
    
    # the collections is used in stead of set and dictionary
    cnt = collections.Counter()
    for word in characters_cn:
        if len(word):
            cnt[word] += 1

    Result = cnt
    count = len(Result)
    return Result, count

# 3 the function which calls the above 2 functions
def stats_text(text):

    # judge if the type of input is correct.
    if type(text) != str:
        raise ValueError('The input text is not the type of String')

    # for chinese words
    Result_cn = stats_text_cn(text)[0]
    count_cn = stats_text_cn(text)[1]

    # for english words
    # remove of the chinese characters in the text
    for character in text:
        if '\u4e00' <= character <= '\u9fff':
            text = text.replace(character,'')
    Result_en = stats_text_en(text)[0] # text is non-chinese text
    count_en = stats_text_en(text)[1]

    Result = Result_cn + Result_en # collections + collections
    count = count_cn + count_en

    return Result,count

# test example 
text = '''
将本地仓库关于本次作业的变 提交为 个commit
通过Github桌 客户端将本地电脑的变 推送到  账户下的作业仓库
回到Github  账户下的作业仓库，向远程公 作业仓库的master分 发起Pull
Request，在提交的 Pull Request 的标题title中填写  所在的钉钉群名
'''

if __name__ == "__main__":
    # a example calling the function for cn_en text using the collections
    try:
        print('the sorted word frequencies for the input text for both chinese and english {}  \n'.
            format(stats_text(text)[0].most_common(stats_text(text)[1])))# stats_text()[1] is the number of the words
    except Exception as e:
        print(e)

    # statistics for the chinese words in the file('tang300.json')
    file_path = '/Users/tsuishihhao/Documents/GitHub/selfteaching-python-camp/exercises/1901050136/d09/mymodule/tang300.json' # absolute address 
    with open(file_path,'r',encoding='utf-8') as f:
        text = f.read()
        try:
            print('the sorted word frequencies for the input text {}  \n'.
                format(stats_text_cn(text)[0].most_common(100))) # most frequent 100 chars 
            # print('number of all characters in the text',stats_text_cn(text)[1]) # stats_text()[1] is the number of the words
        except Exception as e:
            print(e)