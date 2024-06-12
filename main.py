def main():
    book_path = "books/frankenstein.txt"
    book = read_book(book_path)
    char_dict = character_count(book)
    sorted_characters = sort_characters(char_dict)
    
    print(f"--- Begin Report of {book_path} ---")
    print(f"{word_count(book)} words were detected in the document")
    print()

    character_report(sorted_characters)
    print()
    print("--- End of Report ---")

    
def read_book(path_to_book):
    with open(path_to_book) as f:
        file_contents = f.read()
        return file_contents     

def word_count(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def character_count(book):
    characters = {}
    book_lowercase = book.lower()
    for character in book_lowercase:
        if character in characters:
            characters[character] += 1
        else:
            characters[character] = 1
    return characters

def sort_criteria(dict):
    return dict["count"]

def sort_characters(dict):
    sorted_dict = []
    for character in dict:
        char = character
        num = dict[char]
        if char.isalpha():
            sorted_dict.append({"character":char, "count":num})
    sorted_dict.sort(reverse=True, key=sort_criteria)
    return sorted_dict

def character_report(sorted_list):
    for item in sorted_list:
        print(f"The '{item['character']}' was found {item['count']} times")



main()