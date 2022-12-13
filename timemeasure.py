from timeit import timeit

print(timeit("my_func_1", setup="from task4 import my_func_1", number=100000))
print(timeit("my_func_2", setup="from task4 import my_func_2", number=100000))
print(timeit("my_func_new", setup="from task4 import my_func_new", number=100000))

0.004352000076323748
0.0030260002240538597
0.0021982002072036266
