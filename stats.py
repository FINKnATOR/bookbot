def number_of_words(book):
    text = book.split()
    return(len(text))

def number_of_characters(book):
    characters = {}
    for character in book:
        letter = character.lower()
        if letter in characters:
            characters[letter] += 1
        else:
            characters[letter] = 1
    return characters

def sort_on(dict):
    return dict["num"]

def sorted_characters(char_dict):
    char_list = []
    for entry in char_dict:
        char_list.append({"name":entry, "num":char_dict[entry]})
    char_list.sort(reverse=True, key=sort_on)
    return char_list