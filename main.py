from stats import get_word_count
from stats import get_character_count

def get_book_text(book_file):

    with open(book_file) as words:
        book_words = words.read()
        return book_words

def main():
    text = get_book_text("./books/frankenstein.txt")
    word_count = get_word_count(text.split())
    char_count = get_character_count(text.lower())
    print(f"{word_count} words found in the document")
    print(char_count)

main()