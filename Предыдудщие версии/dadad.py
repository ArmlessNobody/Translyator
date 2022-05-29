def rome(res_number):
    temp_temp_text = '';
    i = 1;
    list_res_numbers = [];
    temp_text = str(res_number) + ", ";
    while res_number > 0:
        res_number, number_ = divmod(res_number, 10);
        list_res_numbers.append(number_ * i);
        i = i * 10;
    i = len(list_res_numbers) - 1;
    while i >= 0:
        print(list_res_numbers[i]);
        if list_res_numbers[i] in rome:
            temp_text = temp_text + rome[list_res_numbers[i]];
        i = i - 1;
    return temp_text