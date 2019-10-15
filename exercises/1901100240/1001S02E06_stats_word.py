# This algorithm return the statistic result of the text
# It provide the frequency of every single words
import re
# Define the function
def stats_text_en(en_text):
    # Split the en_text into single words and put them into a list
    en_text=re.split(r"(?:[\s!#$%&\*+,-./:;<=>?@^_`{|}~])",en_text)     #[] sperate the multiple symbol, \s serate the space, ?: exclude the symbol from the list
    # Remove all the empty element from the list
    while '' in en_text:
        en_text.remove('')
    # Count the word use dictionary
    en_count={}     # Create an empty dictionary
    for char in en_text:
        if char not in en_count:   # Set the value of word to 1 if the word not yet in dictionary
            en_count[char] = 1
        else:       # The count plus 1 if the word already in dictionary
            en_count[char] += 1
    # Sorted the dictionary by value in decreasing order
    en_count = sorted(en_count.items(), key = lambda en_count:en_count[1], reverse = True)
    return en_count # Return the dictionary as result

# This algorithm return the statistic result of the text in Chinese
# It provide the frequency of every single character
def stats_text_cn(cn_text):
    cn_text=list(cn_text)       # Transfer the cn_text to list
    # Remove all the special symbol element from the list
    for symbol in "！“”#$%&‘’（）*+，-。/：；、……<=>？@[]《》^_`{|}~\n":
        while symbol in cn_text:        # Remove the element from list as long as it is a special symbol
            cn_text.remove(symbol)
    # Count the word use dictionary
    cn_count={}     # Create an empty dictionary
    for char in cn_text:
        if char not in cn_count:        # Set the value of word to 1 if the word not yet in dictionary
            cn_count[char] = 1
        else:       # The count plus 1 if the word already in dictionary
            cn_count[char] += 1
    # Sorted the dictionary by value in decreasing order
    cn_count = sorted(cn_count.items(), key = lambda cn_count:cn_count[1], reverse = True)
    return cn_count     # Return the dictionary as result

en_string = "The Zen of Python, by Tim PetersBeautiful is better than ugly.Explicit is better than implicit.Simple is better than complex.Complex is better than complicated.Flat is better than nested.Sparse is better than dense.Readability counts.Special cases aren't special enough to break the rules.Although practicality beats purity.Errors should never pass silently.Unless explicitly silenced.In the face of ambxiguity, refuse the temptation to guess.There should be one-- and preferably only one --obvious way to doit.Although that way may not be obvious at first unless you're Dutch.Now is better than never.Although never is often better than *right* now.If the implementation is hard to explain, it's a bad idea.If the implementation is easy to explain, it may be a good idea.Namespaces are one honking great idea -- let's do more of those!"
cn_string='''我冒着严寒，回到相隔二千余里，别了二十余年的故乡去。时候既然是深冬；渐近故乡时，天气又阴晦了，冷风吹进船舱中，呜呜的响，从篷隙向外一望，苍黄的天底下，远近横着几个萧索的荒村，没有一些活气。我的心禁不住悲凉起来了。阿！这不是我二十年来时时记得的故乡？我所记得的故乡全不如此。我的故乡好得多了。但要我记起他的美丽，说出他的佳处来，却又没有影像，没有言辞了。仿佛也就如此。于是我自己解释说：故乡本也如此，——虽然没有进步，也未必有如我所感的悲凉，这只是我自己心情的改变罢了，因为我这次回乡，本没有什么好心绪。'''

print(stats_text_en(en_string))
print(stats_text_cn(cn_string))