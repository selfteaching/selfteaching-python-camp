def add(a, b):
    return a + b


def substructin(a, b):
    return a - b


def multiplication(a, b):
    return a * b


def division(a, b):
    return a / b


first_value = input('请输入数值：')
second_value = input('请输入数值：')
list1 = [int(first_value),int(second_value)]


print("{} + {}".format(list1[0], list1[1]), add(list1[0],list1[1]))
print('{} - {}'.format(list1[0], list1[1]), substructin(list1[0], list1[1]))
print('{} * {}'.format(list1[0], list1[1]), multiplication(list1[0], list1[1]))
print('{} / {}'.format(list1[0], list1[1]), division(list1[0], list1[1]))
