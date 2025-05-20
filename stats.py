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