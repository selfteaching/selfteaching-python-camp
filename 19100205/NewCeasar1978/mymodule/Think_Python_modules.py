import string
import random
def print_grids(n):
    '''本函数用于打印纵横数量相同的方格，例如九宫格，十六宫格等，参数 n 为每行或每列的格子数量'''
    for y in range(1,5*n+2):
        for x in range(1,5*n+2):
            if x % 5 == 1:
                if y % 5 ==1:
                    print('+',end = '')
                else:
                    print('|',end ='')
            else:
                if y % 5 ==1:
                    print('-  ',end = '')
                else:
                    print('   ',end ='')
        print()
#n = int(input('您想每行或列打印几个格子：'))
#print_grids(n)

import math
import turtle #后续函数都要用到的库，在此处导入一次即可，函数中应避免出现 import

def square(t,lenth):
    '''绘制正方形
    t：turtle；
    lenth：边长'''
    for i in range(0,4):
        t.fd(lenth)
        t.lt(90)
    turtle.mainloop()


def polygon(t,lenth,n):
    '''绘制多边形
    t：turtle；
    lenth：边长
    n：边数'''
    for i in range(0,n):
        t.fd(lenth)
        t.lt(360/n)
    turtle.mainloop()


def circle(t,r):
    '''
    绘制圆形
    t：turtle；
    r：半径
    '''
    arc(t,r,360)

def arc(t,r,angle):
    '''绘制圆弧
    t：turtle；
    r：半径；
    angle：角度'''
    n = int(2*math.pi*r/4+3) # 确定适当的多边形数量
    t.lt(angle/2/n) # 与最后一行 t.rt(angle/2/n) 共同减小误差
    for i in range(int(n*angle/360)):
        t.fd(2*math.pi*r/n)
        t.lt(360/n)
    t.rt(angle/2/n)
    
def flower(t,r,n,angle):
    """打印花的图形；
    t:turple 对象；
    r:弧线半径；
    n：花瓣数量；
    angel：弧线的弧度。
    """          
    for i in range(n):
        arc(t,r,angle)
        t.lt(180-angle)
        arc(t,r,angle)
        t.lt(180-angle+360/n)


def pies(t,lenth,n):
    '''
    绘制披萨图形
    t：turtle；
    lenth：半径
    n：边数
    '''
    side = abs(2*lenth*math.sin(float(180/n*math.pi/180))) #计算每个等腰三角形的底边长
    for i in range(n):
        t.fd(lenth)
        t.lt(90+180/n)
        t.fd(side)
        t.lt(90+180/n)
        t.fd(lenth)
        t.lt(180)

def spiral(t,n,b = 500,angle = 10):
    '''
    绘制阿基米德螺旋线
    t：turtle
    n：近似弧线的段数
    angle：近似弧线的角度
    b：控制螺旋线疏密程度，数字越小，螺旋线越密    
    '''
    theta = 0.0
    for i in range(n):        
        r = b*theta*math.pi/180
        arc(t,r,angle)
        theta += 0.1




def koch(t,lenth,n=3):
    '''绘制科赫曲线
    t：turtle；
    length：最外层轮廓的边长；
    n：分型的阶数；
    '''
    if n == 0:
        t.fd(lenth)
        return
    else:
        m = lenth/3
        koch(t,m,n-1)
        t.lt(60)
        koch(t,m,n-1)
        t.rt(120)
        koch(t,m,n-1)
        t.lt(60)
        koch(t,m,n-1)



def factorial(n):
    '''计算 n 的阶乘
    '''
    if n == 0:
        return 1
    else:
        s = 1
        for i in range(1,n+1):
            s = s*i
        return s

def square_root(a):
    '''
    求 a 的平方根
    '''
    x = a / 2
    y = (x + a/x)/2
    while x != y:
        x = y
        y = (x + a/x)/2
    return y

def estimate_pi():
    '''
    计算圆周率的近似值
    '''
    s = 0
    k = 0
    while True:
        t = factorial(4*k)*(1103+26390*k)/factorial(k)**4/396**(4*k)
        if t < 1e-15:
            s = s + t
            break
        else:
            s = s + t
            k += 1
    pi =  1/(2*math.sqrt(2)*s/9801)
    print(k)
    return pi

    
def rotate_word(original_text,n):
    '''凯撒加密程序（移位加密法）
    original_text：需加密的原文
    n：移位的位数，正数为向右移动，负数为向左移动
    '''
    ciphertext = ''
    for original_letter in original_text:
        if original_letter.islower():
            start = ord('a')
            cipher_letter = chr(start + (ord(original_letter) - start + n ) % 26)
        elif original_letter.isupper():
            start = ord('A')
            cipher_letter = chr(start + (ord(original_letter) - start + n ) % 26)
        else:
            cipher_letter = original_letter
        ciphertext += cipher_letter
    return ciphertext



def rotate_word_1(ciphertext,n):
    '''凯撒解密程序（移位加密法）
    ciphertext：需解密的密文
    n：移位的位数，正数为向右移动，负数为向左移动
    '''
    original_text = ''
    for cipher_letter in ciphertext:
        if cipher_letter.islower():
            start = ord('a')
            original_letter = chr(start + (ord(cipher_letter) - start - n ) % 26)
        elif cipher_letter.isupper():
            start = ord('A')
            original_letter = chr(start + (ord(cipher_letter) - start - n ) % 26)
        else:
            original_letter = cipher_letter
        original_text += original_letter
    return original_text



def avoids(word,string):
    '''判断 word 中是否包含 string 中出现的字母，如果不包含，返回 True。
    '''
    for letter in string:
        if letter in word:
            break
    else:
        return True

def exclude(string):
    '''计算所有不包含 string 中所出现字母的单词总数。
    '''
    with open('words.txt') as fin:
        count = 0
        for line in fin:
            word = line.strip()
            if avoids(word,string) == True:
                count += 1
        return count   

# 以下为不包含任意数量字母组合的单词的数量
from itertools import combinations
letters = ('a','b','c','d','e','f','g','h','i','j','k','l','m',\
            'n','o','p','q','r','s','t','u','v','w','x','y','z')
letters_set = tuple(combinations(letters,1)) #本语句控制字母组合的数量
result = {}
for i in letters_set:
    combination = ''.join(i)
    result[combination] = exclude(combination)
combination_min = min(result,key=result.get)
combination_max = max(result,key=result.get)


def uses_only(word,string):
    '''判断 word 中的字母是否都处于 string 中
    '''
    for i in word:
        if i not in string:
            break
    else:
        return True


def uses_all(word,string):
    '''判断 string 中的字母是否都在 word 中出现过
    '''
    for i in string:
        if i not in word:
            break
    else:
        return True


def is_abecedarian(word):
    '''判断 word 中的字母是否按字母表顺序排列
    '''
    for i in range(len(word)-1):
        if word[i] > word[i+1]:
            break
    else:
        return True

def is_triple_double(word):
    '''判断一个单词中是否存在三次连续的重复字母，例如，aabbcc
    '''       
    if len(word) < 6:
        return False
    else:
        for i in range(len(word)-5): #注意此处的 range 边界
            if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
                return True
        return False


def has_duplicates(list_1):
    '''判断一个列表中是否包含重复的元素
    '''
    if len(set(list_1)) != len(list_1):
        return True
    else:
        return False

'''以下程序用随机数的方式验证生日悖论
import numpy
count = 0
n = 100000000
for i in range(n):
    t = numpy.random.randint(365,size = 23)
    if has_duplicates(t):
        count += 1
p = count/n
print(p*100,'%')
'''

def is_bisection(word,list_1):
    '''用对折法判断 word 是否处于 list_1 中
    word：字符串
    list_1：按字母顺序排列的列表
    ''' 
    while len(list_1) > 1:
        word_middle = list_1[int(len(list_1)/2)]
        
        if word == word_middle:
            return True
        elif word > word_middle:
            list_1 = list_1[int(len(list_1)/2):]
        elif word < word_middle:
            list_1 = list_1[:int(len(list_1)/2)]
    if word == list_1[0]:
        return True

def reversal(dic):
    '''将一个字典 dic 的 key 和 value 互换，如果原字典有多个 key 对应一个 value，转换后将多个 key 合并为一个列表
    '''
    dic_rev = {}
    for k in dic:
        v = dic[k]
        if v not in dic_rev:
            dic_rev[v] = [k]
        else:
            dic_rev[v].append(k)
    return dic_rev

def reversal_1(dic):
    '''将一个字典 dic 的 key 和 value 互换，如果原字典有多个 key 对应一个 value，转换后将多个 key 合并为一个列表。
    用 setdefault 方法实现
    '''
    dic_rev = {}
    for k in dic:
        v = dic[k]
        dic_rev.setdefault(v,[]).append(k)
    return dic_rev

def make_wordlist(filename):
    '''将一个 txt 文件中的单词转换为列表。
    目的是供后面进行遍历处理。
    '''
    with open(filename,encoding = 'UTF-8') as fin:
        word_list_clear = []
        s = string.whitespace + string.punctuation
        for line in fin:
            line = line.replace('-',' ').lower()
            word_list = line.split()
            for word in word_list:
                word = word.strip(s)
                word_list_clear.append(word)          
        return word_list_clear

def make_worddic(filename,encoding = 'UTF-8'):
    '''将一个 txt 文件中的单词转换为字典。
    目的是供后面进行遍历处理。
    '''
    with open(filename) as fin:
        word_dic = {}
        s = string.whitespace + string.punctuation
        for line in fin:
            line = line.replace('-',' ').lower()
            word_list = line.split()
            for word in word_list:
                word = word.strip(s)
                word_dic[word] = True
        return word_dic  


def Markov_analysis(filename,orders):
    '''通过一个 txt 文本，利用 Markov_analysis 的方法生成随机文本。
    filename：txt 文件名
    orders：每个前缀的长度
    '''
    word_list_clear = make_wordlist(filename)
    dic_rel = {}
    for i in range(len(word_list_clear)-orders):
        pre = ()
        for j in range(orders):
            pre = pre + (word_list_clear[i+j],)
        
        suf = word_list_clear[i+orders]
        dic_rel.setdefault(pre,[]).append(suf)


    first = random.choice(list(dic_rel))
    print(first)
    pre = first
    suf = random.choice(dic_rel[pre])
    print(pre,suf)
    text_random = ''
    for i in range(len(pre)):
        text_random += pre[i] + ' '
    text_random += ' ' + suf
    print(text_random)
    while pre in dic_rel and len(text_random) < 2000:
        pre = tuple(list(pre)[1:]) + (suf,)
        suf = random.choice(dic_rel[pre])
        text_random = text_random + ' ' + suf

    return text_random

def anagram_sets(filename = 'words.txt'):
    word_dic = make_worddic(filename)
    res = {}
    for word in word_dic:
        chr_list = list(word)
        chr_list.sort()
        signature = ''.join(chr_list)
        res.setdefault(signature,[]).append(word)
    return res    