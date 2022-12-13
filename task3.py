# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(arg_1, arg_2, arg_3):
    print(f'Сумма двух наибольших элементов = '
          f'{(arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)}')


my_func(1, 2, 3)


def my_func_new(arg_1, arg_2, arg_3):
    print(f'Сумма двух наибольших элементов = '
          f'{sum(arg_1, arg_2, arg_3) - min(arg_1, arg_2, arg_3)}')


my_func_new(1, 2, 3)
