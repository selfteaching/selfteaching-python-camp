from mymodule import stats_word

sample_text = '''
BOX是 Btc + eOs + Xin 的缩写，而 BOX 本身，又恰好是中文 “盒子” 的意思。又由于 BOX 是李笑来设计的 ETF 产品，所以江湖戏称 “韭菜盒子”，而 “定投 BOX”，被人们戏称 “总吃韭菜盒子”。
'''

result = stats_word.stats_text(sample_text)

print('统计结果 ==>', result)