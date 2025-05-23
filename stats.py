dict_char = {}
ordened_list = []


def get_text_form(text):
    text_number = text.split()
    replace = " ".join(text_number).lower()
    return replace


def get_num_words(text_form):
    words = len(text_form.split())
    return words


def get_num_char(char_num):
    for i in char_num:
        dict_char.setdefault(i, 0)
        if i in dict_char:
            dict_char[i] += 1
    return dict_char


def get_order_list(dict_char):

    for dict in dict_char:
        key = dict
        value = dict_char[dict]
        dict_list = {"char": key, "num": value}
        ordened_list.append(dict_list)
    ordened_list.sort(reverse=True, key=sort_on)
    for i in ordened_list:
        for item in i:
            if item == "char":
                new_key = i[item]
            else:
                new_value = i[item]

        if new_key.isalpha():
            print(f"{new_key}: {new_value}")


def sort_on(ordened_list):
    return ordened_list["num"]
