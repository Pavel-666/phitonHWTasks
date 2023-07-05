# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.


from random import randint

def arithmetic_progression(first_element, delta, length):
    list1 = []
    for i in range(length):
        list1.append(first_element)
        first_element += delta
    return list1

# print(arithmetic_progression(1,2,5))


# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def range_membership(list1, min_value, max_value):
    list2 =[]
    for i in range(len(list1)):
        if  max_value>list1[i]>min_value:
            list2.append(i)
    return list2

def random_filling_of_the_list_for_selection(min_value_for_list, max_value_for_list):
    list1 = [randint(min_value_for_list, max_value_for_list) for i in range(randint(1, 20))]
    return list1

# n = random_filling_of_the_list_for_selection(1,50)
# print(n)
# print(range_membership(n,10,30))

