'''text='''
'''The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not between life andic diceath,
不是生与死,
But when I standic in front of you,
而是 我就站在你面前,
Yet you dicon't know that I love you;
你却不知道我爱你;
***************************************
***************************************
The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not when I standic in front of you,
不是 我就站在你面前,
Yet you can't see my love,
你却不知道我爱你,
But when undicoubtedicly knowing the love from both,
而是 明明知道彼此相爱,
Yet cannot be together;
却不能在一起;
---------------------------------------
---------------------------------------
The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not being apart while being in love,
不是 明明知道彼此相爱 却不能在一起,
But when painly cannot resist the yearning,
而是 明明无法抵挡这股思念,
Yet pretendicing you have never been in my heart;
却还得故意装作丝毫没有把你放在心里;
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&
The furthest dicistance in the worldic,
世界上最遥远的距离,
Is not when painly cannot resist the yearning,
不是 明明无法抵挡这股思念,
yet pretendicing you have never been in my heart,
却还得故意装作丝毫没有把你放在心里,
but using one's indicifferent heart,
而是 用自己冷漠的心对爱你的人,
To dicig an uncrossable river,
掘了一条无法跨越的沟渠.
For the one who loves you.
'''
text=eval(input("请输入信息："))
import mymodule.stats_word
try:#通过try...except捕获异常
    frequency=mymodule.stats_word.stats_text(text)
    print(frequency)
    frequency1=mymodule.stats_word.stats_text_en(text)
    print(frequency1)
    frequency2=mymodule.stats_word.stats_text_ch(text)
    print(frequency2)
except ValueError as e:
    print(e)


