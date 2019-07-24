import stats_word as sw

a = int(input('请输入需要排序的分词数： '))

with open('D:\\GitHub - Desktop\\selfteaching-python-camp\\19100205\\lihaotian007\\mymodule\\tang300.json','r',encoding = 'UTF-8') as op_tang :
    read_tang = op_tang.read()
    sw.stats_text(read_tang,a)
op_tang.closed