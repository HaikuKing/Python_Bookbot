from stats import (get_word_count, get_character_count, sorted)

def get_book_text(book_file):

    with open(book_file) as words:
        book_words = words.read()
        return book_words

def main():
    location = "books/frankenstein.txt"
    text = get_book_text(f"./{location}")
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