from stats import (get_word_count, get_character_count, sorted)
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

def get_book_text(book_file):

        book_words = book_file.read()
        return book_words

def main():

    with open(sys.argv[1]) as location:
        text = get_book_text(location)
        word_count = get_word_count(text.split())
        char_count = get_character_count(text.lower())
        sort_count = sorted(char_count)
        print_report(location, word_count, sort_count)


def print_report(location, word_count, sort_count):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {location}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sort_count:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()