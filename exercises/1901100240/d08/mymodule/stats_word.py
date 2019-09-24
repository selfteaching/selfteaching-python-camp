# This algorithm return the statistic result of the text
# It provide the frequency of every single words
import re
# Define the function
def stats_text_en(en_text):
    # Split the en_text into single words and put them into a list
    try:
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
    except TypeError:
        print("Error! The input of function stats_text_en should be the form of string. The input now is in ", type(en_text)," type. Please retry and enter a string")

# This algorithm return the statistic result of the text in Chinese
# It provide the frequency of every single character
def stats_text_cn(cn_text):
    try:
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
    except TypeError:
        print("Error! The input of function stats_text_cn should be the form of string. The input now is in ", type(cn_text)," type. Please retry and enter a string")

# This function uses the following encoding: utf-8
# Return a list of strings with English and Chinese words seperatly
def stats_text(string):
    # Seperate the Chinese and English words into two strings by checking ASCII value
    try:
        en_text = "".join(i for i in string if ord(i) < 256).replace("\n", " ")     # ord() returns ASCII or Unicode value, less than 256 will provide the English words
        cn_text = "".join(j for j in string if ord(j) > 256)        # ord() returns ASCII or Unicode value, greater than 256 will provide the Chinese Character
        return [stats_text_en(en_text),stats_text_cn(cn_text)]
    except TypeError:
        print("Error! The input of function stats_text should be the form of string. The input now is in ", type(string)," type. Please retry and enter a string")
