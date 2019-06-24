import os
file_object = open('./d07/text.txt')
file_context = file_object.read()
file_object.close()
print(file_context)