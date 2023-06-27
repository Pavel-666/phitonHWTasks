# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


from random import randint
list1 = [randint(-10, 10) for i in range(randint(1,20))]
list2 = [randint(-10, 10) for i in range(randint(1,20))]
print(list1)
print(list2)
list1 = set(list1)
list2 = set(list2)
finalList = []
for i in list1:
    for j in list2:
        if i == j:
            finalList.append(i)
list.sort(finalList)
print(finalList)
