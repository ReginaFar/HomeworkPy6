# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать,
# вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

from memory_profiler import profile

n = int(input('Введите число от 1 до 9:'))
@profile
def find_sum(n):
    print(n + (n * 10 + n) + (n * 100 + n * 10 + n))

find_sum(n)

n = int(input('Введите число от 1 до 9:'))
@profile
def summa(n):
    summa = n + (n * 10 + n) + (n * 100 + n * 10 + n)
    print(summa)

summa(n)




