import sys

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    words = text.split()
    character_count = {}
    for word in words:
        word = word.lower()
        for i in range(0, len(word)):
            if word[i].isalpha():
                if word[i] in character_count:
                    character_count[word[i]] += 1
                else:
                    character_count[word[i]] = 1
    return character_count

def sort_on(dict):
    return dict["count"]
            
def generate_list_of_dicts(character_dict):
    list_of_dict = []
    for key in character_dict.keys():
        list_of_dict.append({ "char": key, "count": character_dict[key] })
    list_of_dict.sort(reverse=True, key=sort_on)
    return list_of_dict

def generate_report(book_name, word_count, list_of_dict):
    text = f"--- Begin report of {book_name} ---"
    text += "\n"
    text += f"{word_count} words found in the document"
    text += "\n\n"
    for dict in list_of_dict:
        char = dict["char"]
        count = dict["count"]
        text += f"The {char} character was found {count} times\n"
    text += "--- End report ---"
    print(text)
    


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    character_count = count_characters(text)
    list_of_dicts = generate_list_of_dicts(character_count)
    generate_report(book_path, word_count, list_of_dicts)

if __name__ == '__main__':
    sys.exit(main())