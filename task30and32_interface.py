from HWTask30and32 import *
from tkinter import *

window = Tk()
window.title('задачи с рекурсией')
window.geometry('900x600')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

first_lb = Label(
    frame,
    font='times 25',
    text="заполнение массива "
)
first_lb.grid(row=1, column=1)

first_lb = Label(
    frame,
    font='times 25',
    text="элементами "
)
first_lb.grid(row=2, column=1)

first_lb = Label(
    frame,
    font='times 25',
    text="арифметической прогрессии"
)
first_lb.grid(row=3, column=1)

first_element_1 = Label(
    frame,
    font='times 15',
    text='с какого элемента начинать заполнение?'
)
first_element_1.grid(row=4, column=1)

first_element_2 = Entry(
    frame,
    font='times 15',
)
first_element_2.grid(row=4, column=2, pady=5)


delta_1 = Label(
    frame,
    font='times 15',
    text="с каким шаогм заполнять?"
)
delta_1.grid(row=5, column=1)

delta_2 = Entry(
    frame,
    font='times 15',
)
delta_2.grid(row=5, column=2, pady=5)

length_1 = Label(
    frame,
    font='times 15',
    text="сколько чисел надо заполнить?"
)
length_1.grid(row=6, column=1)

length_2 = Entry(
    frame,
    font='times 15',
)
length_2.grid(row=6, column=2, pady=5)


def first_button():
    first_element = int(first_element_2.get())
    delta = int(delta_2.get())
    length = int(length_2.get())
    progression = arithmetic_progression(first_element, delta, length)
    button = Label(
        frame,
        font='times 20',
        text=F"                                                                                                        "
    )
    button.grid(row=8, column=2)
    button = Label(
        frame,
        font='times 20',
        text=F"прогрессия от {first_element} c щагом {delta}:"
    )
    button.grid(row=8, column=2)
    button = Label(
        frame,
        font='times 20',
        text='                                                                                                         '
    )
    button.grid(row=9, column=2)
    button = Label(
        frame,
        font='times 20',
        text=progression
    )
    button.grid(row=9, column=2)


cal_btn = Button(
    frame,
    font='times 20',
    text='посчитать',
    command=first_button
)
cal_btn.grid(row=7, column=2)


first_lb = Label(
    frame,
    font='times 25',
    text="поиск индексов"
)
first_lb.grid(row=10, column=1)

min_value_for_list_1 = Label(
    frame,
    font='times 15',
    text="нижняя граница списка"
)
min_value_for_list_1.grid(row=11, column=1)

min_value_for_list_2 = Entry(
    frame,
    font='times 15',
)
min_value_for_list_2.grid(row=11, column=2, pady=5)


max_value_for_list_1 = Label(
    frame,
    font='times 15',
    text="верхняя граница списка"
)
max_value_for_list_1.grid(row=12, column=1)

max_value_for_list_2 = Entry(
    frame,
    font='times 15',
)
max_value_for_list_2.grid(row=12, column=2, pady=5)

min_value_1 = Label(
    frame,
    font='times 15',
    text='минимальное значение искомого'
)
min_value_1.grid(row=13, column=1)

min_value_2 = Entry(
    frame,
    font='times 15'
)
min_value_2.grid(row=13, column=2, pady=5)

max_value_1 = Label(
    frame,
    font='times 15',
    text='максимальное значение искомого'
)
max_value_1.grid(row=14, column=1)

max_value_2 = Entry(
    frame,
    font='times 15'
)
max_value_2.grid(row=14, column=2, pady=5)


def second_button():
    min_value_for_list = int(min_value_for_list_2.get())
    max_value_for_list = int(max_value_for_list_2.get())
    min_value = int(min_value_2.get())
    max_value = int(max_value_2.get())
    random_list = random_filling_of_the_list_for_selection(min_value_for_list, max_value_for_list)
    range1 = range_membership(random_list, min_value, max_value)
    button = Label(
        frame,
        font='times 12',
        text=F"                                                                                                        "
    )
    button.grid(row=16, column=2)
    button = Label(
        frame,
        font='times 12',
        text=F"список: {random_list}"
    )
    button.grid(row=16, column=2)
    button = Label(
        frame,
        font='times 15',
        text=F"                                                                                                        "
    )
    button.grid(row=17, column=2)
    button = Label(
        frame,
        font='times 15',
        text=F"выборка: {range1}"
    )
    button.grid(row=17, column=2)


second_btn = Button(
    frame,
    text='вычислить',
    font='times 20',
    command=second_button
)
second_btn.grid(row=15, column=2)

window.mainloop()
