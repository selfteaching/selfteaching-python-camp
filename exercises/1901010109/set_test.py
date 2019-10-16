import matplotlib.pyplot as plt
from matplotlib_venn import venn2

admins = {'Moose', 'Joker', 'Joker'}
moderators = {'Ann', 'Chris', 'Jane', 'Moose', 'Zero'}

v = venn2(subsets=(admins, moderators), set_labels=('admins', 'moderators'))
v.get_lable_by_id('11').set_text('\n'.join(admins.intersection(moderators)))
v.get_lable_by_id('10').set_text('\n'.join(admins.difference(moderators)))
v.get_lable_by_id('01').set_text('\n'.join(admins.symmetric_difference(moderators)))

plt.show()