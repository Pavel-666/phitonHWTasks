import HWTask26and28
from tkinter import *

window = Tk()
window.title('задачи с рекурсией')
window.geometry('800x600')

frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

first_lb = Label(
    frame,
    font='times 25',
    text="функция возведения в степень"
)
first_lb.grid(row=1, column=1)

substruct1 = Label(
    frame,
    font='times 15',
    text="введитте возволимое в степень число"
)
substruct1.grid(row=3, column=1)

substruct2 = Entry(
    frame,
    font='times 15',
)
substruct2.grid(row=3, column=2, pady=5)


index1 = Label(
    frame,
    font='times 15',
    text="степень числа"
)
index1.grid(row=4, column=1)

index2 = Entry(
    frame,
    font='times 15',
)
index2.grid(row=4, column=2, pady=5)


def first_button():
    first = int(substruct2.get())
    second = int(index2.get())
    pow1 = HWTask26and28.exponentiation(first, second)
    button = Label(
        frame,
        font='times 25',
        text=F"{first} в степени {second} = {pow1}"
    )
    button.grid(row=6, column=2)


cal_btn = Button(
    frame,
    font='times 20',
    text='возвести в степень',
    command=first_button
)
cal_btn.grid(row=5, column=2)

first_lb = Label(
    frame,
    font='times 25',
    text="функция сложения"
)
first_lb.grid(row=7, column=1)

term1_1 = Label(
    frame,
    font='times 15',
    text="первое слагаемое"
)
term1_1.grid(row=8, column=1)

term2_1 = Entry(
    frame,
    font='times 15',
)
term2_1.grid(row=8, column=2, pady=5)


term1_2 = Label(
    frame,
    font='times 15',
    text="второе слагаемое"
)
term1_2.grid(row=9, column=1)

term2_2 = Entry(
    frame,
    font='times 15',
)
term2_2.grid(row=9, column=2, pady=5)


def second_button():
    first = int(term2_1.get())
    second = int(term2_2.get())
    sum1 = HWTask26and28.sum(first, second)
    button = Label(
        frame,
        font='times 25',
        text=F"{first} + {second} = {sum1}"
    )
    button.grid(row=11, column=2)


second_btn = Button(
    frame,
    text='сложить',
    font='times 20',
    command=second_button
)
second_btn.grid(row=10, column=2)

window.mainloop()
