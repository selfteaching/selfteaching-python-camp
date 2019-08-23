# This algorithm return the statistic result of the text
# It provide the frequency of every single words
from collections import Counter
# Define the function
def stats_text_en(en_text,count):
    try:
        en_text = "".join(i for i in en_text if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122).replace("\n", " ")     # ord() returns ASCII or Unicode value, less than 256 will provide the English words
        # Count the word use Counter
        try:
            en_count = Counter(en_text).most_common(count)         # Create an counter
            return en_count # Return the counter as result
        except TypeError:
            print("Error! The second input of function stats_text_en should be the form of integer. The input now is in ", type(en_text)," type. Please retry and enter a integer")
    except TypeError:
        print("Error! The first input of function stats_text_en should be the form of string. The input now is in ", type(en_text)," type. Please retry and enter a string")

# This algorithm return the statistic result of the text in Chinese
# It provide the frequency of every single character
def stats_text_cn(cn_text,count):
    try:
        cn_text = "".join(j for j in cn_text if ord(j) > 256)        # ord() returns ASCII or Unicode value, greater than 256 will provide the Chinese Character
        try:
            cn_count = Counter(cn_text).most_common(count)         # Create an counter
            return   cn_count   # Return the counter as result
        except TypeError:
            print("Error! The second input of function stats_text_cn should be the form of integer. The input now is in ", type(cn_text)," type. Please retry and enter a integer")
    except TypeError:
        print("Error! The first input of function stats_text_cn should be the form of string. The input now is in ", type(cn_text)," type. Please retry and enter a string")

# This function uses the following encoding: utf-8
# Return a list of strings with English and Chinese words seperatly
def stats_text(string,count):
    # Seperate the Chinese and English words into two strings by checking ASCII value
    try:
        en_text = "".join(i for i in string if ord(i) < 256).replace("\n", " ")     # ord() returns ASCII or Unicode value, less than 256 will provide the English words
        cn_text = "".join(j for j in string if ord(j) > 256)        # ord() returns ASCII or Unicode value, greater than 256 will provide the Chinese Character
        return [stats_text_en(en_text,count),stats_text_cn(cn_text,count)]
    except TypeError:
        print("Error! The first input of function stats_text should be the form of string. The input now is in ", type(string)," type. Please retry and enter a string")
