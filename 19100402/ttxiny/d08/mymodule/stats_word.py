def stats_text_en(a):
  if type(a)==str:
    a=a.replace(',', ' ').replace('.', ' ').replace('--', ' ').replace('!', ' ').replace('*', ' ')
    a=a.lower()
    a=a.split()
    dic={}
    for i in a:
      b=a.count(i)
      c={i:b}
      dic.update(c)
    dic=sorted(dic.items(),key=lambda x:x[1],reverse=True)
    print(dic)
  else:
    raise ValueError

def stats_text_cn(a): 
  if type(a)==str:
    a=a.replace('，','').replace('。','')
    b={}
    for i in a:
        if u'\u4e00'<=i<=u'\u9fff':
              b[i]=a.count(i)+1
        else:
              b[i]=1
    return b
    print(sorted(stats_text_cn(a).items(),key=lambda i:i[1],reverse=True))
  else:
    raise ValueError
  
def stats_text(a):
    stats_text_cn(a)
    stats_text_en(a)

