# This algorithm is to do the statistic of frequency of Chinese characters in tang300
# Using the user-defined algrorithm 'stats_word' and package 'json'
import stats_word
import json

# Imput the tang300.json documents and transfer into form of [{dict},{dict},{dict}]
with open('/Users/yanning/Documents/GitHub/selfteaching-python-camp/exercises/1901100240/d10/mymodule/tang300.json','r+',encoding = "utf-8") as f:
    tang_load = json.load(f)

# Create a empty string and use it as storage.
tang_text=""
# Using loop to combine all dict.values() into the storage string
for unit in tang_load:      # Unit will be each dictionary in the list
    for char in unit.values():      # Char will be each values of the dictionary in form ['values','values','values','values']
        for content in str(char):       # content will be each element in the list Char
            if ord(content) > 256 and content not in "！“”#$%&‘’（）*+，-。/：；、……<=>？@[]［］《》^_`{|}~\n":     # Only count the Chinese characters without any symbol
                tang_text += str(content)       # Store the string into the storage string tang_text

# Doing the statistic of frequncy of each Chinese characters and make it a list
print(stats_word.stats_text_cn(tang_text,20))