from stats import count_words, count_chars, sorted_dict
import sys


def get_book_text(filepath):
    contents = ""

    with open(filepath, "r", encoding="utf-8") as f:
        contents = f.read()

    return contents


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    prog_name = sys.argv[0]
    book_path = sys.argv[1]

    contents = get_book_text(book_path)
    print(count_words(contents))

    char_map = count_chars(contents)
    sorted_chars = sorted_dict(char_map)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")


main()
