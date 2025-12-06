from textwrap import dedent
from stats import get_num_words, sort_character_counts
import stats
import sys

def get_book_text(path: str):
    with open(path, mode="r", encoding="utf-8") as f:
        return f.read()


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(path=book_path)
    num_words = get_num_words(book_text)
    char_dict = stats.get_character_counts(book_path)
    report_text = dedent(f"""
                         ============ BOOKBOT ============
                         Analyzing book found at {book_path}
                         ----------- Word Count ----------
                         Found {num_words} total words
                         --------- Character Count -------
                         """).strip()
    print(report_text)
    for count_info in sort_character_counts(char_dict):
        if count_info["char"].isalpha():
            print(f"{count_info["char"]}: {count_info['num']}")


if __name__ == "__main__":
    main()
