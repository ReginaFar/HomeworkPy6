# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта,
# сделать замеры времени, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
# что вы сделали и чего удалось добиться

from timeit import timeit

# 1. Нахождение максимального элемента в списке:


def find_max(mas):
    max_el = mas[0]
    for i in range(len(mas)):
        if mas[i] > max_el:
            max_el = mas[i]
    print(max_el)


def find_max_new(mas):
    max_el = max(mas)
    print(max_el)


find_max([100, 39, 25, 111])
find_max_new([100, 39, 25, 111])

print(timeit("find_max", globals=globals(), number=100000))
print(timeit("find_max_new", globals=globals(), number=100000))

"""
Получили следующие замеры:
find_max - 0.005072099999999996
find_max_new - 0.0024410999999999947
Функция find_max_new выполняется в два раза быстрее за счёт использования
встроенной функции max
"""

# 2. Находим в списке числа, кратные 11


def find_num(lst):
    new_lst = []
    for num in range(len(lst)):
        if lst[num] % 11 == 0:
            new_lst.append(lst[num])
    print(new_lst)


def find_num_new(lst):
    new_lst = [num for num in lst if num % 11 == 0]
    print(new_lst)


find_num([190, 121, 20, 22, 1331])
find_num_new([190, 121, 20, 22, 1331])

print(timeit("find_num", globals=globals(), number=1000000))
print(timeit("find_num_new", globals=globals(), number=1000000))

"""
Получили следующие замеры:
find_num - 0.021680599999999998
find_num_new - 0.0158192
Функция find_num_new выполняется быстрее благодаря использованию list comprehension
"""
