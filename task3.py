# 3) Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def max_sum(arg_1, arg_2, arg_3):
    print(f'Сумма двух наибольших элементов = '
          f'{(arg_1 + arg_2 + arg_3) - min(arg_1, arg_2, arg_3)}')


max_sum(
    int(input('Первое число:')),
    int(input('Второе число:')),
    int(input('Третье число:')),
)


def max_sum_new(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)


max_sum_new(
    int(input('Первое число:')),
    int(input('Второе число:')),
    int(input('Третье число:')),
)
