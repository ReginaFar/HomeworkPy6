# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def max_sum(arg_1, arg_2, arg_3):
    print(f'Сумма двух наибольших элементов = '
          f'{(arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)}')


max_sum(10, 12, 13)


def max_sum_new(*args):
    print(sum(sorted(list(args), reverse=True)[:2]))


max_sum_new(10, 12, 13)


def get_max(*args):
    lst = list(args)
    i = 0
    res = 0
    while i != 2:
        max_val = max(lst)
        res += max_val
        lst.remove(max_val)
        i += 1
    print(res)


get_max(10, 12, 13)
