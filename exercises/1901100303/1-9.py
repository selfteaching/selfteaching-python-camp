
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = 'all'
import sys
#print(sys.builtin_module_names)
print("_sre" in sys.builtin_module_names)
print("math" in sys.builtin_module_names)

for row in range(1,10):
    for col in range(1,10):
        prod=row*col
        if prod<10:
            print(' ',end='')
        print(row*col,' ',end='')
    print()    


