from mymodule import stats_word

sample_text='''
了不起的盖茨比

我年纪还轻，阅历不深的时候，我父亲教导过我一句话，
我至今还念念不忘。

“每逢你想要批评任何人的时候，”他对我说，
“你就记住，这个世界上所有的人，并不是个个都有过你拥有的那些优越条件。”

The Great Gatsby
In my younger and more vulnerable years my father gave me some advice
that I've been turning over in my mind ever since.
"Whenever you feel like criticising any one,"he told me,
"just remember that all the people in this world haven't had the advantages
that you've had."
'''

result = stats_word.stats_text(sample_text)
print('统计结果\n',result)
                     