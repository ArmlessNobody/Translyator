from tkinter import *;
import dictionary;

class numbers(object):


    def __init__(self, numbers, rank):
        self.numbers = numbers;
        self.rank = rank;


def insert():
    flag_soixante = 0;
    flag_hundreds = 0;
    flag_break = 0;
    flag_break2 = 0;
    res_number = 0;
    str_ = txt.get() + " ";
    flag = 0;
    temp_str_ = "";
    list_numbers = [];
    list_numbers_rank = []
    for i in range(0, len(str_)):
        if str_[i] != " ":
            temp_str_ += str_[i];
            flag = 1;
            if (str_[i+1] == " ") and (flag == 1):
                list_numbers.append(temp_str_);
                temp_str_ = "";


    j=0;

    for i in range(0, len(list_numbers)):
        if list_numbers[i] in _units:
            number = numbers(_units[list_numbers[i]], 1 );
            list_numbers_rank.append(number);
        else:
            if list_numbers[i] in units:
                number = numbers(units[list_numbers[i]], 2 );
                list_numbers_rank.append(number);
            else:
                if list_numbers[i] in _tens:
                    number = numbers(_tens[list_numbers[i]], 3);
                    list_numbers_rank.append(number);
                else:
                    if list_numbers[i] in tens:
                        number = numbers(tens[list_numbers[i]], 4);
                        list_numbers_rank.append(number);
                    else:
                        if list_numbers[i] in hundreds:
                            number = numbers(hundreds[list_numbers[i]], 5);
                            list_numbers_rank.append(number);
                        else:
                            if list_numbers[i] != "et":
                                j = i;
                                flag_break = 1;
                                break;





    i = 0;
    while i < (len(list_numbers_rank)):
        if i + 2 < len(list_numbers_rank):
            if list_numbers_rank[i] == 4 and  list_numbers[i+1] == "et" and list_numbers[i+2] == "un":
                res_number= list_numbers_rank[i].numbers + list_numbers_rank[i+2].numbers;
            elif list_numbers[i] == "soixante" and list_numbers[i + 1] == "dix" and list_numbers_rank[i+2].rank == 2:
                res_number += list_numbers_rank[i].numbers + list_numbers_rank[i+1].numbers + list_numbers_rank[i+2].numbers;
                flag_soixante = 1;
            elif list_numbers[i] == "quatre" and list_numbers[i+1] == "vingts" and list_numbers_rank[i+2].rank == 3:
                res_number += list_numbers_rank[i].numbers * list_numbers_rank[i+1].numbers + list_numbers_rank[i+2].numbers;
                i = i + 2;
                flag_soixante == 1
        if i + 1 < len(list_numbers_rank):
            if list_numbers[i] == "quatre" and list_numbers[i+1] == "vingts":
                res_number = list_numbers_rank[i].numbers * list_numbers_rank[i+1].numbers;
            elif (list_numbers_rank[i].rank == 1 or list_numbers_rank[i].rank == 2) and list_numbers_rank[i + 1].rank == 5:
                if  list_numbers[i] == "un" and list_numbers[i+1] == "cent":
                    flag_break2 = 1;
                    temp_text = "Нельзя использовать единиц 'un' перед разрядом сотен 'cent'!";
                    break;
                elif list_numbers[i] == "un" and list_numbers[i+1] == "cents":
                    flag_break2 = 1;
                    temp_text = "Нельзя использовать разряд единиц 'un' перед разрядом сотен 'cents'!";
                    break;
                elif list_numbers[i+1] == "cent":
                    flag_break2 = 1;
                    temp_text = "Нельзя использовать разряд единиц '"  + list_numbers[i] + "' перед разрядом сотен 'cent'!";
                    break;
                flag_hundreds = 1;
                res_number+= list_numbers_rank[i].numbers * list_numbers_rank[i+1].numbers;

            elif list_numbers_rank[i].rank <= list_numbers_rank[i + 1].rank:
                if list_numbers_rank[i].rank == 1:
                    text = "Разряд единиц";
                elif list_numbers_rank[i].rank == 2:
                    text = "Разряд единиц";
                elif list_numbers_rank[i].rank == 3:
                    text = "Разряд десятков";
                elif list_numbers_rank[i].rank == 4:
                    text = "Разряд десятков";
                elif list_numbers_rank[i].rank == 5:
                    text = "Разряд сотен";
                if list_numbers_rank[i + 1].rank == 1:
                    text2 = "разрядом единиц";
                elif list_numbers_rank[i + 1].rank == 2:
                    text2 = "разрядом единиц";
                elif list_numbers_rank[i + 1].rank == 3:
                    text2 = "разрядом десятков";
                elif list_numbers_rank[i + 1].rank == 4:
                    text2 = "разрядом десятков";
                elif list_numbers_rank[i + 1].rank == 5:
                    text2 = "разрядом сотен";

                flag_break2 = 1;
                temp_text = text + " '" + list_numbers[i] + "' " + "не может стоять перед " + text2 + " '" + \
                            list_numbers[i + 1] + "'!";
                break;

            elif list_numbers_rank[i].rank == 4 and list_numbers_rank[i + 1].rank == 3:
                if list_numbers[i] == "soixante":
                        flag_soixante = 1;
                        res_number +=  list_numbers_rank[i].numbers + list_numbers_rank[i+1].numbers;
                else:
                    flag_break2 = 1;
                    temp_text = "Разряд десятков '" + list_numbers[i] + "' " + "не может стоять перед разрядом '" + list_numbers[i + 1] + "'!";
                    break;
            elif list_numbers_rank[i].rank == 3 and list_numbers[i] != "dix" and  (list_numbers_rank[i + 1].rank == 1 or list_numbers_rank[i + 1].rank == 2):
                    flag_break2 = 1;
                    temp_text = "Разряд десятков '" + list_numbers[i] + "' " + "не может стоять перед разрядом единиц '" + list_numbers[i + 1] + "'!";
                    break;
            else:
                if list_numbers_rank[i].rank == 3:
                    if list_numbers[i] == "dix" and list_numbers_rank[i+1].rank == 1:
                        temp_text = "Разряд десятков 'dix' не может стоять перед разрядом единиц '" + list_numbers[i+1] + "'!";
                        flag_break2 = 1;
                        break;
                    res_number += list_numbers_rank[i].numbers;
                elif list_numbers_rank[i].rank == 4:
                    if list_numbers[i+1] == 'un':
                        temp_text = "Разряд десятков '" + list_numbers[i]  + "' не может стоять перед разрядом единиц '" + list_numbers[ i + 1] + "'!";
                        flag_break2 = 1;
                        break;
                    res_number += list_numbers_rank[i].numbers;
                elif flag_hundreds == 0:
                    if list_numbers_rank[i].rank == 5:
                        res_number += list_numbers_rank[i].numbers;




        elif list_numbers_rank[i].rank == 1:
            res_number += list_numbers_rank[i].numbers;
        elif flag_soixante == 0:
            if list_numbers_rank[i].rank == 2:
                res_number += list_numbers_rank[i].numbers;
        elif flag_soixante == 0:
            if list_numbers_rank[i].rank == 3:
                res_number += list_numbers_rank[i].numbers;
        elif list_numbers_rank[i].rank == 4:
            res_number += list_numbers_rank[i].numbers;
        elif flag_hundreds == 0:
            if list_numbers_rank[i].rank == 5:
                res_number += list_numbers_rank[i].numbers;

        i = i +1;

    if flag_break2 == 1:
        lbl.configure(text=temp_text);
    elif flag_break == 1:
            res = "Слово '" + list_numbers[j] + "' не распознано, введите число заново!"
            lbl.configure(text=res);
    else:
        lbl.configure(text=res_number);

window = Tk()

window.title("Translator.ru");
window.geometry('650x150');
lbl = Label(window, text="Введите число на фрацузском языке, используя пробелы и не используя '-' :", font='Times 14');
lbl.pack(side= 'top', anchor = W, ipadx=4, padx=1, ipady=3, pady=3);
f = Frame();
f.pack(side = TOP);
txt = Entry(f,width = 50, font='Times 12');
txt.pack(side = LEFT, anchor = N, fill = 'x', ipadx=7, padx=5, ipady=7, pady=1);
insert_btn = Button(f, text="Ввод",  width = 25, command = insert,  font='Times 12');
insert_btn.pack( side = 'left', ipadx=3, padx=6, ipady=2, pady=0);

f2 = Frame();
f2.pack(side = BOTTOM, fill = X);

lbl = Label(f2, text="", font='Times 13', bg = 'white', width = 450);
lbl.pack(side= LEFT, anchor = W, ipadx=5, padx=5, ipady=5, pady=5);

lbl2 = Label(window, text="Резултат работы транслятора:", font='Times 14');
lbl2.pack(side= 'bottom', anchor = W, ipadx=4, padx=4, ipady=3, pady=3);


window.mainloop();