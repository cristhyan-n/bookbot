from stats import get_num_words, get_num_char


def get_book_text():
    with open("books/frankenstein.txt") as f:
        file_contens = f.read()
        return file_contens


def main():
    file_text = get_book_text()
    char_num = get_num_words(file_text)
    get_num_char(char_num)


main()
