import re

def main ():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    new_letters = get_lower_letters(text)
    letter_count = get_letter_count(new_letters)
    
    print (letter_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_lower_letters(text):
    lower_list = []
    lowered_string = text.lower()
    lowered_list = re.sub(r'[^a-z ]','',lowered_string)
    lowered_list = list(lowered_list)
    
    return (lowered_list)

def get_letter_count(letter):
    letter_dict = {}
    for x in letter:
        if x in letter_dict:
            letter_dict[x] += 1
        else:
            letter_dict[x] = 1
    return letter_dict




main()