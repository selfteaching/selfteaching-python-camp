a_list = []
a_list.append(1)
a_list.append(2)
print(a_list, f'has a length of {len(a_list)}')

b_list = list(range(1, 9))
b_list.append(11)
print(b_list, f'has a length of {len(b_list)}')

c_list = [2**x for x in range(8)]
print(c_list, f'has a length of {len(c_list)}')
