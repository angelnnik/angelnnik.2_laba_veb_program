import random

def func_1(chislo):
    naoborot = 0
    pr_ch = chislo  
    while pr_ch > 0:
        des = pr_ch % 10
        naoborot = naoborot * 10 + des
        pr_ch = pr_ch // 10
    return (naoborot == chislo)

def func_2(lst):
    spisok_2 = []
    spisok_3 = []
    spisok_5 = []
    for i in lst:
        if i % 2 == 0:
            spisok_2.append(i)
        if i % 3 == 0:
            spisok_3.append(i)
        if i % 5 == 0:
            spisok_5.append(i)
    return [spisok_2, spisok_3, spisok_5]

def func_3(chislo):
    naoborot = 0
    pr_ch = chislo
    if pr_ch < 0:
        pr_ch = pr_ch + (-2) * pr_ch
    while pr_ch > 0:
        des = pr_ch % 10
        naoborot = naoborot * 10 + des
        pr_ch = pr_ch // 10
    if chislo < 0:
        naoborot = naoborot - 2 * naoborot
    return naoborot

def f(x1, st1, ch1):
    return x1 ** st1 - ch1
def proiz(x2, st2, ch2):
    return st2 * x2 ** (st2-1)
def func_4(st, ch):
    x = 1
    kor = abs(f(x, st, ch))
    while kor > 1e-5:
        x = x - f(x, st, ch)/proiz(x, st, ch)
        kor = abs(f(x, st, ch))
    return x
           
import random
def func_5(x):
    schet = 0
    for i in range(1, x):
        if x % i == 0:
            schet = schet + 1
    return (schet == 1)

            
    
'''print(func_1(int(input("Введите число для проверки на пaлиндром"))))'''

'''mylist = [8, 12, 15, 6, 16, 25]
print(func_2(mylist))'''

'''print(func_3(int(input("Введите число для получения обратного числа"))))'''


'''print(func_4(int(input("Введите степень корня")), int(input("Введите подкоренное число"))))'''

'''ran = random.randint(1, 100000)
print(ran, " ", func_5(ran))'''





