# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растёт на круглой грядке, причём кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод —
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль,
# находясь перед некоторым кустом заданной во входном файле грядки.


from random import randint
from tkinter import *
from tkinter import messagebox
from random import randint

window = Tk()
window.title('выбор одинаковых элементов зи двух множеств')
window.geometry('600x300')


list1 = [randint(10, 5000) for i in range(randint(3,20))]
print(list1)
numberBush = randint(0,len(list1)-1)
print(numberBush)
if numberBush + 1 == len(list1) :
    nextBush = 0
else: nextBush = numberBush + 1
if numberBush - 1 == 0:
    earlyBush = len(list1) - 1
else: earlyBush = numberBush - 1
# print(nextBush)
# print(earlyBush)
summHarvest = list1[numberBush] + list1[nextBush] + list1[earlyBush]
print(summHarvest)


frame = Frame(
    window,
    padx=10,
    pady=10
)
frame.pack(expand=True)

height_lb = Label(
    frame,
    text="урожайность каждого дерева"
)
height_lb.grid(row=1, column=2)

height_lb = Label(
    frame,
    text = str(list1)
)
height_lb.grid(row=2, column=2)


height_lb = Label(
    frame,
    text="указанное дерево сбора"
)
height_lb.grid(row=3, column=2)

height_lb = Label(
    frame,
    text = str(numberBush+1)
)
height_lb.grid(row=4, column=2)

height_lb = Label(
    frame,
    text="сумма общего сбора за один подход"
)
height_lb.grid(row=5, column=2)

height_lb = Label(
    frame,
    text = str(summHarvest)
)
height_lb.grid(row=6, column=2)

window.mainloop()
