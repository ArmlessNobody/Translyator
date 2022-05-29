from tkinter import *;
from dictionary import *;

class numbers(object):

    def __init__(self, numbers, rank):
        self.numbers = numbers;
        self.rank = rank;

def Eror(list_numbers_rank, list_numbers_rank2, list_numbers, list_numbers2):


    if list_numbers_rank.rank == 1:
        text = "Разряд единиц";
    elif list_numbers_rank.rank == 2:
        text = "Разряд единиц";
    elif list_numbers_rank.rank == 3:
        text = "Разряд десятков";
    elif list_numbers_rank.rank == 4:
        text = "Разряд десятков";
    elif list_numbers_rank.rank == 5:
        text = "Разряд сотен";

    if list_numbers_rank2.rank == 1:
        text2 = "разрядом единиц";
    elif list_numbers_rank2.rank == 2:
        text2 = "разрядом единиц";
    elif list_numbers_rank2.rank == 3:
        text2 = "разрядом десятков";
    elif list_numbers_rank2.rank == 4:
        text2 = "разрядом десятков";
    elif list_numbers_rank2.rank == 5:
        text2 = "разрядом сотен";



    temp_text = text + " '" + list_numbers + "' " + "не может стоять перед " + text2 + " '" + \
                list_numbers2 + "'!";

    return temp_text;

def Rome(res_number):
    i = 1;
    list_res_numbers = [];
    temp_text = str(res_number) + ", ";
    while res_number > 0:
        res_number, number_ = divmod(res_number, 10);
        list_res_numbers.append(number_ * i);
        i = i * 10;
    i = len(list_res_numbers) - 1;
    while i >= 0:
        if list_res_numbers[i] in rome:
            temp_text = temp_text + rome[list_res_numbers[i]];
        i = i - 1;
    return temp_text

def insert():
    flag_break = 0;
    flag_break2 = 0;
    res_number = 0;
    flag = 0;
    res_number = int(res_number);
    str_ = txt.get().lower() + " ";
    flag_null = 0;
    temp_str_ = "";
    list_numbers = [];
    list_numbers_rank = []
    for i in range(0, len(str_)):
        if str_[i] != " ":
            temp_str_ += str_[i];
            flag = 1;
            if (str_[i + 1] == " ") and (flag == 1):
                list_numbers.append(temp_str_);
                temp_str_ = "";

    if len(list_numbers) == 0:
        flag_null = 1;
    j = 0;

    for i in range(0, len(list_numbers)):
        if list_numbers[i] in units_one:
            number = numbers(units_one[list_numbers[i]], 1);
            list_numbers_rank.append(number);
        elif list_numbers[i] in units:
            number = numbers(units[list_numbers[i]], 2);
            list_numbers_rank.append(number);
        elif list_numbers[i] in tens_one:
            number = numbers(tens_one[list_numbers[i]], 3);
            list_numbers_rank.append(number);
        elif list_numbers[i] in tens:
            number = numbers(tens[list_numbers[i]], 4);
            list_numbers_rank.append(number);
        elif list_numbers[i] in hundreds:
            number = numbers(hundreds[list_numbers[i]], 5);
            list_numbers_rank.append(number);
        elif list_numbers[i] == "et":
            number = numbers(-1, -1);
            list_numbers_rank.append(number)
        else:
            j = i;
            flag_break = 1;
            break;

    i = 0;
    if flag_null == 1:
        lbl.configure(text="Ничего не было введено, повторите ввод!");
    elif flag_break == 1:
        res = "Слово '" + list_numbers[j] + "' не распознано, введите число заново!"
        lbl.configure(text=res);
    else:
        while i < (len(list_numbers_rank)):
            if list_numbers[i] == "et":
                if i == 0:
                    flag_break2 = 1;
                    temp_text = "Союз 'et' не может стоять в начале числа!";
                    break;
                elif i + 1 == len(list_numbers_rank) or list_numbers[i+1] != "un":
                    flag_break2 = 1;
                    temp_text = "После союза 'et' обязательно должен стоять разряд единиц 'un'!";
                    break;
                elif i - 2 >= 0 and list_numbers[i-2] == "quatre" and list_numbers[i-1] == "vingt":
                    flag_break2 = 1;
                    temp_text = "После 'quatre vingt' союз 'et' не употребляется!";
                    break;
                elif i -1 >= 0 and (list_numbers_rank[i-1].rank == 1 or list_numbers_rank[i-1].rank == 2):
                    flag_break2 = 1;
                    temp_text = "После разряда единиц '" + list_numbers[i-1] + "' союз 'et' не употребляется!";
                    break;

            elif (i + 2 < len(list_numbers_rank)) and list_numbers[i] == "quatre" and list_numbers[i + 1] == "vingt" and \
                    list_numbers[i + 2] == "un":
                res_number += list_numbers_rank[i].numbers * list_numbers_rank[i + 1].numbers + list_numbers_rank[
                    i + 2].numbers;
                i = i + 2;
            elif (i + 2 < len(list_numbers_rank)) and list_numbers_rank[i] == 4 and list_numbers[i + 1] == "et" and list_numbers[i + 2] == "un":

                res_number = list_numbers_rank[i].numbers + list_numbers_rank[i + 2].numbers;

            elif (i + 1 < len(list_numbers_rank)) and list_numbers[i] == "quatre" and list_numbers[i + 1] == "vingt":
                if i + 2 == len(list_numbers_rank):
                    temp_text = Eror(list_numbers_rank[i], list_numbers_rank[i + 1], list_numbers[i], list_numbers[i + 1]);
                    flag_break2 = 1;
                    break;
                elif list_numbers[i + 2] == 'un':
                    temp_text = "Разряд десятков '" + list_numbers[i + 1] + "' не может стоять перед разрядом единиц '" + \
                                list_numbers[i + 2] + "'!";
                    flag_break2 = 1;
                    break;

                res_number += list_numbers_rank[i].numbers * list_numbers_rank[i + 1].numbers;
                i = i + 1;
            elif (i + 1 < len(list_numbers_rank)) and list_numbers[i] == "quatre" and list_numbers[i + 1] == "vingts":
                if i + 2 != len(list_numbers_rank):
                    flag_break2 = 1;
                    temp_text = "После разряда десятков 'vingts' не может идти что-либо! Возможно вы имели в виду 'vingt'!";
                    break;
                elif i - 1 > 0 and list_numbers[i-1] == "vingt":
                    flag_break2 = 1;
                    temp_text = "После разряда десятков 'vingt' не может идти число 'quatre vingts'!";
                    break;
                else:
                    res_number += list_numbers_rank[i].numbers * list_numbers_rank[i + 1].numbers;
                    i = i + 1;
            elif (i + 1 < len(list_numbers_rank)) and i+1 == 1 and (list_numbers_rank[i].rank == 1 or list_numbers_rank[i].rank == 2) and list_numbers_rank[i + 1].rank == 5:

                if list_numbers[i] == "un" and list_numbers[i + 1] == "cents":
                    flag_break2 = 1;
                    temp_text = "Нельзя использовать разряд единиц 'un' перед разрядом сотен 'cents'!";
                    break;
                elif list_numbers[i + 1] == "cent":
                    if i + 1 + 1 == len(list_numbers_rank):
                        flag_break2 = 1;
                        temp_text = "Нельзя использовать разряд единиц '" + list_numbers[i] + "' перед разрядом сотен 'cent'!";
                        break;
                elif i + 2 < len(list_numbers_rank) and list_numbers[i+2] == "et":
                    flag_break2 = 1;
                    temp_text = "Нельзя использовать союз 'et' после разряда сотен '" + list_numbers[i+1] + "'!";
                    break;

                res_number += list_numbers_rank[i].numbers * list_numbers_rank[i + 1].numbers;
                i = i + 1;
            elif (i + 1 < len(list_numbers_rank)) and list_numbers[i] != "et" and  ((list_numbers_rank[i].rank <= list_numbers_rank[i + 1].rank) or (list_numbers_rank[i].rank == 2 and list_numbers_rank[i+1].rank == 1)):
                temp_text = Eror(list_numbers_rank[i], list_numbers_rank[i + 1], list_numbers[i], list_numbers[i + 1]);
                flag_break2 = 1;
                break;

            elif (i + 1 < len(list_numbers_rank)) and list_numbers_rank[i].rank == 4 and list_numbers_rank[i + 1].rank == 3:
                if list_numbers[i] == "soixante":
                    res_number += list_numbers_rank[i].numbers
                else:
                    flag_break2 = 1;
                    temp_text = "Разряд десятков '" + list_numbers[i] + "' " + "не может стоять перед разрядом десятков '" + \
                                list_numbers[i + 1] + "'!";
                    break;
            elif (i + 1 < len(list_numbers_rank)) and list_numbers_rank[i].rank == 3 and list_numbers[i] != "dix" and (
                    list_numbers_rank[i + 1].rank == 1 or list_numbers_rank[i + 1].rank == 2):
                flag_break2 = 1;
                temp_text = "Разряд десятков '" + list_numbers[i] + "' " + "не может стоять перед разрядом единиц '" + \
                            list_numbers[i + 1] + "'!";
                break;
            elif (i + 1 < len(list_numbers_rank)) and list_numbers_rank[i].rank == 3:
                if list_numbers[i + 1] == "et":
                    temp_text = "Разряд десятков '" +  list_numbers[i] +"' не может стоять перед союзом 'et'!";
                    flag_break2 = 1;
                    break;
                elif list_numbers_rank[i+1].rank == 1:
                    temp_text = "Разряд десятков 'dix' не может стоять перед разрядом единиц '" + list_numbers[
                        i + 1] + "'!";
                    flag_break2 = 1;
                    break;
                res_number += list_numbers_rank[i].numbers;
            elif (i + 1 < len(list_numbers_rank)) and list_numbers_rank[i].rank == 4:
                if list_numbers[i + 1] == 'un':
                    temp_text = "Разряд десятков '" + list_numbers[
                        i] + "' не может стоять перед разрядом единиц '" + list_numbers[i + 1] + "'!";
                    flag_break2 = 1;
                    break;
                res_number += list_numbers_rank[i].numbers;


            elif list_numbers_rank[i].rank == 1 or list_numbers_rank[i].rank == 2 or list_numbers_rank[i].rank == 3 or list_numbers_rank[i].rank == 4:

                res_number += list_numbers_rank[i].numbers;

            elif list_numbers_rank[i].rank == 5:
                if list_numbers[i] == "cents":
                    temp_text = "Нельзя использовать разряд сотен 'cents', если перед ним не идет разряд единиц!"
                    flag_break2 = 1;
                    break;
                elif (i + 1 ) < len(list_numbers_rank) and list_numbers[i+1] == "et":
                    temp_text = "Нельзя использовать союз 'et' после разряда сотен 'cent'!"
                    flag_break2 = 1;
                    break;
                else:
                    res_number += list_numbers_rank[i].numbers;


            i = i + 1;


        if flag_break2 == 1:
            lbl.configure(text=temp_text);
        else:
            lbl.configure(text=Rome(res_number));

window = Tk()

window.title("Translyator.ru");
window.geometry('650x150');
lbl = Label(window, text="Введите число на фрацузском языке, используя пробелы и не используя '-' :", font='Times 14');
lbl.pack(side='top', anchor=W, ipadx=4, padx=1, ipady=3, pady=3);
f = Frame();
f.pack(side=TOP);
txt = Entry(f, width=50, font='Times 13');
txt.pack(side=LEFT, anchor=N, fill='x', ipadx=7, padx=5, ipady=7, pady=1);
insert_btn = Button(f, text="Ввод", width=25, command=insert, font='Times 12');
insert_btn.pack(side='left', ipadx=3, padx=6, ipady=2, pady=0);

f2 = Frame();
f2.pack(side=BOTTOM, fill=X);

lbl = Label(f2, text="", font='Times 13', bg='white', width=450);
lbl.pack(side=LEFT, anchor=W, ipadx=5, padx=5, ipady=5, pady=5);

lbl2 = Label(window, text="Результат работы транслятора:", font='Times 14');
lbl2.pack(side='bottom', anchor=W, ipadx=4, padx=4, ipady=3, pady=3);

window.mainloop();