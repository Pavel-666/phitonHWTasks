# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества.
# m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.


from tkinter import *
from tkinter import messagebox
from random import randint

window = Tk()
window.title('выбор одинаковых элементов зи двух множеств')
window.geometry('600x300')


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

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="первое сгенерированное множество"
)
height_lb.grid(row=1, column=2)

height_lb = Label(
    frame,
    text = str(list1)
)
height_lb.grid(row=2, column=2)


height_lb = Label(
    frame,
    text="второе сгенерированное множество"
)
height_lb.grid(row=3, column=2)

height_lb = Label(
    frame,
    text = str(list2)
)
height_lb.grid(row=4, column=2)

height_lb = Label(
    frame,
    text="пересечение множеств"
)
height_lb.grid(row=5, column=2)

height_lb = Label(
    frame,
    text = str(finalList)
)
height_lb.grid(row=6, column=2)

window.mainloop()