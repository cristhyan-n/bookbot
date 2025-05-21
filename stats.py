dict_char = {}


def get_num_words(text):
    text_number = text.split()
    replace = " ".join(text_number).lower()
    return replace


def get_num_char(char_num):
    for i in char_num:
        dict_char.setdefault(i, 0)
        if i in dict_char:
            dict_char[i] += 1

    return print(dict_char)
