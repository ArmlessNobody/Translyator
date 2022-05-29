from tkinter import *
from tkinter.ttk import Combobox



class FoxArrayException(Exception):
    pass


class FoxArray:
    """описание класса для определения одномерных массивов строк фиксированной длины"""

    def __init__(self, length: int, str_length=35):
        """
        :param length: длина массива
        :param str_length: длина строки в массиве
        """
        if not isinstance(length, int):
            raise FoxArrayException('-20001 фыр-фыр!')
        if not isinstance(str_length, int):
            raise FoxArrayException('-20002 фыр-фыр!')
        self.__str_length = str_length
        self.__secret_trixie_is_best_pony = ['' for _ in range(length)]

    def __setitem__(self, index: int, value: str):
        if not isinstance(index, int):
            raise FoxArrayException('-20003 int != {}'.format(type(index)))
        if not isinstance(value, str):
            raise FoxArrayException('-20004 фыр-фыр!')
        if len(value) > self.__str_length:
            raise FoxArrayException('-20005 строка сильно длинная')
        self.__check_overflow(index)
        self.__secret_trixie_is_best_pony[index] = value

    def __getitem__(self, index: int):
        if not isinstance(index, int):
            raise FoxArrayException('-20006 int != {}'.format(type(index)))
        self.__check_overflow(index)
        return self.__secret_trixie_is_best_pony[index]

    def __check_overflow(self, index: int):
        if not (0 <= index < len(self.__secret_trixie_is_best_pony)):
            raise FoxArrayException('-20007 выход за границы массива')

    def print(self, index: int):
        """печать (вывод на экран) элементов массива"""
        print(self[index])

    def print_array(self):
        """печать (вывод на экран) всего массива"""
        print(self)

    def __str__(self):
        return ' '.join(self.__secret_trixie_is_best_pony)


def insert_btn_(arr):
    arr[int(combo.get())] = txt.get()
    print(arr[int(combo.get())]);


M = 3;
arr = FoxArray(M)



window = Tk()

window.title("Massive_String.ru")


lbl = Label(window, text="Введите строку, а затем нажмите 'Ввод' :", font='Times 14')
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3)

f = Frame()
f.pack(side=TOP)


txt = Entry(f, font='Times 13')
txt.pack(side=LEFT, anchor=N, fill='x', ipadx=3, padx=6, ipady=7, pady=3)

combo_list = []
for i in range(0, M):
    combo_list.append(i)

combo = Combobox(f, state="readonly")
combo.pack(side=LEFT, ipadx=7, padx=5, ipady=7, pady=1)
combo["values"] = combo_list
combo.current(0);

insert_btn = Button(f, text="Ввод", width=2, command = lambda : insert_btn_(arr) ,  font='Times 14')
insert_btn.pack(side=BOTTOM, ipadx=3, padx=6, ipady=2, pady=3)

insert_btn = Button(f, text="Вывод данных", width=2, command = lambda : arr[int(combo.get())].print() ,  font='Times 14')
insert_btn.pack(side=BOTTOM, ipadx=3, padx=6, ipady=2, pady=3)


window.mainloop()






