def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = count_letters(text)
    report = generate_report(letter_count)
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document")
    print("")
    for letter in report:
        print(f"The '{letter[0]}' character was found {letter[1]} times")
    print("--- End Report ---")

def generate_report(letters):
    report = []
    for letter in letters:
        if letter.isalpha():
            report.append([letter,letters[letter]])
    report.sort()
    return report

def count_letters(text):
    letters = {}
    for letter in str(text):
        letter = letter.lower()
        if letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    return letters

def count_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()
