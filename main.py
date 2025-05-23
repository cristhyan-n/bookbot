from stats import get_num_words, get_num_char, get_order_list, get_text_form
import sys


def get_book_text():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        with open(sys.argv[1]) as f:
            file_contens = f.read()
            return file_contens


def main():
    file_text = get_book_text()
    get_num_words(file_text)
    char_num = get_text_form(file_text)
    order_list = get_num_char(char_num)

    print(" BOOKBOT ".center(40, "="))
    print(f"Analyzing book found at {sys.argv[1]}...")
    print(" Word Count ".center(40, "-"))
    print(f"Found {len(file_text.split())} total words")
    print(" Character Count ".center(40, "-"))

    get_order_list(order_list)
    print(" END ".center(40, "-"))


main()
