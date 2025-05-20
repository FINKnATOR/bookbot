from stats import number_of_words

def get_book_text(filepath):
    with open(filepath) as book_text:
        return book_text.read()




book_text = get_book_text("books/frankenstein.txt")
word_count = number_of_words(book_text)

def main():
    print(f"{word_count} words found in the document")

main()