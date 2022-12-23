# 2) Из ваших заданий в уроках 1-5 найти 2-3 скрипта, сделать замеры памяти, оптимизировать,
# вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ, что вы сделали и чего удалось добиться

from memory_profiler import profile
from random import randint

# 1. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка.
# Для формирования списка использовать генератор.


@profile
def sort_list():
    list_1 = [randint(0, 1000) for i in range(100000)]
    result = [list_1[i]
              for i in range(1, len(list_1)) if list_1[i] > list_1[i - 1]]
    return result


@profile
def sort_list_new():
    list_1 = [randint(0, 1000) for i in range(100000)]
    result = [list_1[i]
              for i in range(1, len(list_1)) if list_1[i] > list_1[i - 1]]
    del list_1
    return result


sort_list()
sort_list_new()
"""
В результате получили следующие замеры:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    10     20.3 MiB     20.3 MiB           1   @profile
    11                                         def sort_list():
    12     23.6 MiB      3.3 MiB      100003       list_1 = [randint(0, 1000) for i in range(100000)]
    13     24.5 MiB      0.9 MiB      100002       result = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i-1]]
    14     24.5 MiB      0.0 MiB           1       return result
    
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    18     20.8 MiB     20.8 MiB           1   @profile
    19                                         def sort_list_new():
    20     23.4 MiB      2.6 MiB      100003       list_1 = [randint(0, 1000) for i in range(100000)]
    21     24.0 MiB      0.6 MiB      100002       result = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i-1]]
    22     23.1 MiB     -0.9 MiB           1       del list_1
    23     23.1 MiB      0.0 MiB           1       return result

При помощи удаления инкремента удалось добиться снижения используемой памяти.
"""

# 2.Представлен список чисел. Определить элементы списка, не имеющие повторений.
# Сформировать итоговый массив чисел, соответствующих требованию.
# Элементы вывести в порядке их следования в исходном списке


@profile
def sorting():
    my_list = [randint(0, 10) for i in range(100000)]
    new_list = [i for i in my_list if my_list.count(i) == 1]
    return (new_list)


@profile
def sorting_new():
    my_list = [randint(0, 10) for i in range(100000)]
    result = [i for i in my_list if my_list.count(i) == 1]
    my_list = None
    return (result)


sorting()
sorting_new()

"""
В результате получили следующие замеры:

Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    57     20.3 MiB     20.3 MiB           1   @profile
    58                                         def sorting():
    59     22.2 MiB  -3819.1 MiB      100003       my_list = [randint(0, 10) for i in range(100000)]
    60     22.2 MiB  -2887.3 MiB      100003       new_list = [i for i in my_list if my_list.count(i) == 1]
    61     22.1 MiB     -0.1 MiB           1       return(new_list)
    
    
Line #    Mem usage    Increment  Occurrences   Line Contents
=============================================================
    63     20.3 MiB     20.3 MiB           1   @profile
    64                                         def sorting_new():
    65     21.6 MiB      1.3 MiB      100003       my_list = [randint(0, 10) for i in range(100000)]
    66     21.6 MiB  -2661.2 MiB      100003       result = [i for i in my_list if my_list.count(i) == 1]
    67     20.3 MiB     -1.3 MiB           1       my_list = None
    68     20.3 MiB      0.0 MiB           1       return(result)
    
    Снизили количество используемой памяти, присвоив списку my_list значение None
"""
