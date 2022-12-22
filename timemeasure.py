# 1) Из ваших заданий в уроках 1-5 найти 2-3 скрипта,
# сделать замеры времени, оптимизировать, вновь выполнить замеры и ОПИСАТЬ СЛОВАМИ,
# что вы сделали и чего удалось добиться

from timeit import timeit

print(timeit("my_func_1", setup="from task4 import my_func_1", number=1000000))
print(timeit("my_func_2", setup="from task4 import my_func_2", number=1000000))
print(timeit("my_func_new", setup="from task4 import my_func_new", number=1000000))

"""
При вводе чисел 2 и -1 получили следующие значения:

"""

# my_func_1 - 0.004352000076323748
# my_func_2 - 0.0030260002240538597
# my_func_new - 0.0021982002072036266

"""
В новой функции my_func_new использовала встроенную функцию возведения в степень,
за счет этого уменьшилось время выполнения программмы.
 
"""


print(timeit("max_sum", setup="from task3 import max_sum", number=100000))
print(timeit("max_sum_new", setup="from task3 import max_sum_new", number=100000))
print(timeit("get_max", setup="from task3 import get_max", number=100000))

# max_sum - 0.00546270003542304
# max_sum_new - 0.002946999855339527

"""
В новой функции max_sum_new при помощи функции min нашла минимальное из трех 
чисел и при помощи функции remove удалила его из списка. Далее при помощи
функции sum нашла сумму двух оставшихся элементов списка.За счет использования
встроенных функций уменьшилось время выполнения программы.

"""
