from stats import get_word_count
from stats import get_character_count
from stats import sorted

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
    print(f"""============ BOOKBOT ============
    Analyzing book found at {location}...
    ----------- Word Count ----------
    Found {word_count} total words
    --------- Character Count -------
    {sort_count}
    ============= END ===============""")

main()