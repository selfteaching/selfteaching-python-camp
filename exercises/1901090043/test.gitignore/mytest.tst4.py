import random
list_1 = []
for items in range(1,101):
    list_1.append(items)
#print(list_1)
new_list = random.sample(list_1,3)
print(sorted(new_list))

with open('/Users/my-mac/desktop/local.txt','w',encoding="utf-8") as file_object:
    file_object.write("i love you !\n")
    file_object.write("i love you too!")