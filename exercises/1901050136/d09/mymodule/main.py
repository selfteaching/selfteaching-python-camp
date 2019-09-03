import stats_word as s
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
            format(s.stats_text(text)[0].most_common(s.stats_text(text)[1])))# stats_text()[1] is the number of the words
    except Exception as e:
        print(e)

    # statistics for the chinese words in the file('tang300.json')
    file_path = '/Users/tsuishihhao/Documents/GitHub/selfteaching-python-camp/exercises/1901050136/d09/mymodule/tang300.json' # absolute address 
    with open(file_path,'r',encoding='utf-8') as f:
        text = f.read()
        try:
            print('the sorted word frequencies for the input text of tang300: \n{} '.
                format(s.stats_text_cn(text)[0].most_common(100))) # most frequent 100 chars 
            # print('number of all characters in the text',stats_text_cn(text)[1]) # stats_text()[1] is the number of the words
        except Exception as e:
            print(e)