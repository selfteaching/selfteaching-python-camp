text='''
The Zen of Python, by Tim Peters


Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated. 9 Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambxiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do
it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
'''
# Replace the better with worse in the text
better_to_worse = text.replace('better', 'worse')

# Remove the word which contain 'ea'
def delete_ea(Str):
    # Convert the string to list
    Str_list = Str.split()
    for word in Str_list:
        if 'ea' in word:
            num = Str_list.index(word)
            del Str_list[num]
    return Str_list

no_ea_words = delete_ea(better_to_worse)


# Swapcase the words 
def swap_case(List):
    swapcase_list = []
    for word in List:
        word = word.swapcase()
        swapcase_list.append(word)
    return swapcase_list

swapcase_words = swap_case(no_ea_words)

# a...z sequence the words
def sequence_list(List):
    # remove the punctuation in the word
    a_list = []
    for word in List:
        word = word.strip('!.*--')
        a_list.append(word)
    # make the words in a to z sequence
    a_list.sort() 
    return a_list

a_z_sequence = sequence_list(swapcase_words)

