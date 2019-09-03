from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

s = """Name,Age,Location
John,18,New York
Mike,22,San Francisco
Janny,25,Miami
Sunny,21,Shanghai"""

r = s.splitlines()[2]
print(r)
#print(r.split())
print(r.split(sep=',')) # r.split(',')作用相同
print(r.split(sep=',', maxsplit=0))

m = ''
t = ['P','y','t','h','o','n']
print(m.join(t))