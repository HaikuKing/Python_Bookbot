def get_book_text(book_file):

    with open(book_file) as words:
        book_words = words.read()
        return book_words

def main():
    text = get_book_text("./books/frankenstein.txt")
    print(text)

main()