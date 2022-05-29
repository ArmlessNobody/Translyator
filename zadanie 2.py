from tkinter import *;


def insert():
    list_txt = [];
    list_txt2 = [];
    str_ = txt.get() + " ";
    str2_ = txt2.get() + " ";
    flag = 0;
    result = "";
    temp_str_ = "";
    for i in range(0, len(str_)):
        if str_[i] != " ":
            temp_str_ += str_[i];
            flag = 1;
            if (str_[i + 1] == " ") and (flag == 1):
                list_txt.append(temp_str_);
                temp_str_ = "";

    for i in range(0, len(str2_)):
        if str2_[i] != " ":
            temp_str_ += str2_[i];
            flag = 1;
            if (str2_[i + 1] == " ") and (flag == 1):
                list_txt2.append(temp_str_);
                temp_str_ = "";

    if len(list_txt) == 0:
        result = "В первую строку не было ничего введено, повторите ввод!";
    elif len(list_txt2) == 0:
        result = "Во вторую строку не было ничего введено, повторите ввод!";

    else:
        if len(list_txt) > len(list_txt2):
            for i in range(0, len(list_txt2)):
                result += list_txt[i] + " " + list_txt2[i] + " ";
            for i in range(len(list_txt2), len(list_txt) ):
                result += " " + list_txt[i];

        if len(list_txt2) > len(list_txt):
            for i in range(0, len(list_txt)):
                result += list_txt[i] + " " + list_txt2[i] + " ";
            for i in range(len(list_txt), len(list_txt2)):
                result += " " + list_txt2[i];

    lbl.configure(text = result);


window = Tk()

window.title("Translyator.ru");
window.geometry('500x250');
lbl = Label(window, text="Введите первую и вторую строку, а затем нажмите 'Ввод' :", font='Times 14');
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3);
f = Frame();
f.pack(side=TOP);
txt = Entry(f, font='Times 13');
txt.pack(side = TOP, anchor=N, fill='x', ipadx=3, padx=6, ipady=7, pady=3);
txt2 = Entry(f, font='Times 13');
txt2.pack(side= TOP, anchor=N, fill='x', ipadx=3, padx=6, ipady=7, pady=3);
insert_btn = Button(f, text="Ввод", width=60, command=insert, font='Times 14');
insert_btn.pack(side='left', ipadx=3, padx=6, ipady=2, pady=3);
f2 = Frame();
f2.pack(side=BOTTOM, fill=X);

lbl = Label(f2, text="", font='Times 13', bg='white', width=450);
lbl.pack(side=LEFT, anchor=W, ipadx=5, padx=5, ipady=5, pady=5);

lbl2 = Label(window, text="Результат работы программы:", font='Times 14');
lbl2.pack(side='bottom', anchor=W, ipadx=4, padx=4, ipady=3, pady=3);


window.mainloop();