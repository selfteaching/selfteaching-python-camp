import hashlib, os
from mymodule.Think_Python_modules import reversal_1
def walk(dirname,dir_list = []):
    
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)

        if os.path.isfile(path):
            dir_list.append(path)
        else:
            walk(path)
    return dir_list



def md5sum(filename):
    fin = open(filename,'rb')
    fc = fin.read()
    fin.close()
    fmd5 = hashlib.md5(fc)
    return fmd5.hexdigest()

def dir_duplicates(dirname):
    dir_list = walk(dirname)
    md5_dic = {}
    for filename in dir_list:
        if '.mp3' in filename:
            md5_dic[filename] = md5sum(filename)
    return md5_dic

md5_dic = dir_duplicates('audio')
print(md5_dic)
res = reversal_1(md5_dic)
print(res)
for v in res:
    if len(res[v]) > 1:
        print(res[v])

