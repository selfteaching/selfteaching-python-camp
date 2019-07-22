import re
def multiply_divide(s):
    ret = float(s.split('*')[0]) * float(s.split('*')[1]) if '*' in s else float(s.split('/')[0]) / float(
        s.split('/')[1])
    return ret

def remove_md(s):
    if '*' not in s and '/' not in s:
        return s
    else:
        k = re.search(r'-?[\d\.]+[*/]-?[\d\.]+', s).group()
        s = s.replace(k, '+' + str(multiply_divide(k))) if len(re.findall(r'-', k)) == 2 else s.replace(k, str(
            multiply_divide(k)))
        return remove_md(s)

def add_sub(s):
    l = re.findall('([\d\.]+|-|\+)', s)
    if l[0] =='-':
        l[0] = l[0] + l[1]          
        del l[1]
    sum = float(l[0])
    for i in range(1, len(l), 2):    
        if l[i] == '+' and l[i + 1] != '-':
            sum += float(l[i + 1])
        elif l[i] == '+' and l[i + 1] == '-':
            sum -= float(l[i + 2])
        elif l[i] == '-' and l[i + 1] == '-':
            sum += float(l[i + 2])
        elif l[i] == '-' and l[i + 1] != '-':
            sum -= float(l[i + 1])
    return sum

def basic_operation(s):
    s = s.replace(' ', '')
    return add_sub(remove_md(s))     

def calculate(expression):
    if not re.search(r'\([^()]+\)', expression):
        return basic_operation(expression)
    k = re.search(r'\([^()]+\)', expression).group()
    expression = expression.replace(k, str(basic_operation(k[1:len(k) - 1])))
    return calculate(expression)
 





                            
            






    
