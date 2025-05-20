from stats import number_of_words
from stats import number_of_characters
from stats import sorted_characters
import sys

if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

def get_book_text(filepath):
    with open(filepath) as book_text:
        return book_text.read()


book_text = get_book_text(sys.argv[1])
word_count = number_of_words(book_text)
total_chars = number_of_characters(book_text)
total_sorted_chars = sorted_characters(total_chars)

def main():
    

    print("============ BOOKBOT ============")
    print(f"Analysing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for character in total_sorted_chars:
        if character["name"].isalpha():
            print(f"{character["name"]}: {character["num"]}")
    print("============= END ===============")

main()