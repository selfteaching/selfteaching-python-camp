

class Kangaroo():
    def __init__(self,name,content = 1):
        self.name = name
        if content == 1:
            content = []
        self.pouch_content = content

    def __str__(self):
        t = [self.name + ' has following content:']
        for obj in self.pouch_content:
            t.append(object.__str__(obj))
        return '\n'.join(t)
        
    def put_in_pouch(self,item):
        self.pouch_content.append(item)

kanga = Kangaroo('Kanga')
roo = Kangaroo('Roo')
kanga.put_in_pouch('wallet')
kanga.put_in_pouch('car key')
kanga.put_in_pouch(roo)

print(kanga)
print(roo)