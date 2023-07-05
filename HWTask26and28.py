# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
# *Пример:*
# 2 2
#     4


def exponentiation(substruct, index):
    if index == 0:
        return 1
    else:
        # print(substruct, index)
        return substruct * exponentiation(substruct, index - 1)



def sum(a, b):
    if b == 0:
        return a
    else:
        return sum(a + 1, b - 1)