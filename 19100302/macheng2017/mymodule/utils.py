from os import path
import pathlib 
import json

path_file = path.dirname(path.realpath(__file__))

def decoding_json(file_name):
    text = ''
    with open(path_file+'/'+file_name) as f:
        read_data = f.read()
    f.closed

    read_data = json.loads(read_data) 

    for item in read_data:
       text += item['contents'] + item['type'] + item['author']
    return text
# print(read_data)