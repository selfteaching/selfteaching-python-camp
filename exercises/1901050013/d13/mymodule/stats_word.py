import re
import jieba
from collections import Counter
def stats_text_en(text):
    """Count the English words in the text."""
    if not isinstance(text,str): # Detect if the text is a string.
        raise ValueError("please input a string.") # If not, raise error.
    text1 = re.sub('[^A-Za-z]',' ',text) # Remove the non-English characters in the text.
    text2 = text1.split() # Convert the string type to the list type.
    return Counter(text2).most_common() # Count the times of each word in the list. Sort the words in the descending order according to the times of words. Return the result.



def stats_text_cn(text):
    """Count the Chinese characters in the text."""
    if not isinstance(text,str): # Detect if the text is a string.
        raise ValueError("please input a string.") # If not, raise error.
    text1 =''.join(re.findall(u'[\u4e00-\u9fff]+', text))  # Get the Chinese characters from the text.
    text2 = jieba.cut(text1,cut_all=False) # use jieba to cut the characters into words.
    text3 = [x for x in text2 if len(x)>= 2] # Convert the string type to the list type. # pick out the length of words that contain at least two characters.
    return Counter(text3).most_common(10) # Count the times of each character in the list. Sort the character in the descending order according to the times of characters. Return the result. 



def stats_text(text):
    """Count the English and Chinese characters in the text."""
    if not isinstance(text,str): # Detect if the text is a string.
        raise ValueError("please input a string.") # If not, raise error.
    return stats_text_en(text) + stats_text_cn(text)







