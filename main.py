import sys

from stats import chars_dict_to_sorted_list, get_chars_dict, get_num_words


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    chars_sorted = chars_dict_to_sorted_list(chars_dict)
    print_report(book_path, num_words, chars_sorted)


def get_book_text(path: str) -> str:
    with open(path) as f:
        return f.read()


def print_report(
    path: str, word_count: int, sorted_list: list[tuple[str, int]]
) -> None:
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")


main()
