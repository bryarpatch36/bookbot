import re

def main ():
    book_path = input("Please enter the path to the book: ")
    text = get_book_text(book_path)
    letter_total = get_letter_total(text)
    new_letters = get_lower_letters(text)
    letter_count = get_letter_count(new_letters)
    nice_report = get_report(letter_count,book_path,letter_total,)
    
    print (nice_report)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def get_letter_total(letters):
    split_list = letters.split()
    count = len(split_list)
    return count


def get_lower_letters(text):
    lower_list = []
    lowered_string = text.lower()
    lowered_list = re.sub(r'[^a-z]','',lowered_string)
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

def sort_on(dict):
    return dict["count"]



def get_report(dict,path,count,):
    letter_list = []
    for char, z in dict.items():
        letter_list.append({"char": char, "count":z})
    letter_list.sort(reverse=True, key=sort_on)
    
    report = (f"--- Begin report of {path} ---\n")
    report += (f"{count} words found in the document\n")
    for y in letter_list:
        report += (f"The '{y['char']}' character was found {y['count']} times\n")
    report += (f"--- End report ---")
    
    
    return report






main()