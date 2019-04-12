def  calculate(s_eq)
     ...
     :param  s_eq: 不带括号的格式化列表
     :return: 计算结果
     ...
     if '*' or '-' in s_eq:
         s_eq = remove_mjultiplication_division(s_eq)
     if '+' or '-' in s_eq:
         s_eq = remove_plus_minus(s_eq)
     return s_eq 