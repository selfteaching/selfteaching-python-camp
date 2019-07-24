import re

text = '''
The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''


# d5_exercise_string


# change "better" into "worse", and "\n" into " ", then remove "ea"
T = text.replace("better", "worse").replace("ea", "").replace("\n", " ").strip()

# remove symbol
i = re.compile("[\.\-\*\!\,\']")
rm_sybol = i.sub("", T)

# split
text_to_list = rm_sybol.split(" ")
text_to_list.remove("")

# swapcase in list
text_swapcase = [x.swapcase() for x in text_to_list]

# sort
text_swapcase.sort()
for t in text_swapcase:
    print(t, end=" ")
print()

# A A AMBXIGUITY AND ARE ARENT AT BAD BE BE BE BRK BTS BY CASES COMPLEX COMPLICATED COUNTS DENSE DO DO ENOUGH EXPLAIN EXPLAIN EXPLICITLY FACE FIRST GOOD GRT GUESS HARD HONKING ID ID ID IMPLEMENTATION IMPLEMENTATION IMPLICIT IS IS IS IS IS IS IS IS IS IS IT IT ITS LETS MAY MAY MORE NESTED NEVER NEVER NEVER NOT NOW OBVIOUS OBVIOUS OF OF OF OFTEN ONE ONE ONE ONLY PASS PRACTICALITY PREFERABLY PURITY REFUSE RIGHT RULES SHOULD SHOULD SILENCED SILENTLY SPECIAL SY TEMPTATION THAN THAN THAN THAN THAN THAN THAN THAN THAT THE THE THE THE THE THOSE TO TO TO TO TO UGLY UNLESS WAY WAY WORSE WORSE WORSE WORSE WORSE WORSE WORSE WORSE YOURE aLTHOUGH aLTHOUGH aLTHOUGH bUTIFUL cOMPLEX dUTCH eRRORS eXPLICIT fLAT iF iF iN nAMESPACES nOW pETERS pYTHON rDABILITY sIMPLE sPARSE sPECIAL tHE tHERE tIM uNLESS zEN



# d5_exercise_stats_text.py

# create dictionary
sort_list = [(x, text_to_list.count(x)) for x in set(text_to_list)]
sort_dict = dict(sort_list)

print(sort_dict) # {'do': 2, 'good': 1, 'Butiful': 1, 'Tim': 1, 'silenced': 1, ...

# #$%$%@$#%!#@#&*…… 
print(sorted(sort_dict.items(), key=lambda x: x[1], reverse=True))