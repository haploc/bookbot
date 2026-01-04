def count_words(file_contents):
    wordlist = file_contents.split()
    return len(wordlist)

def count_characters(file_contents):
    charactercount = dict()
    for char in file_contents:
        lowerchar = char.lower()
        if lowerchar in charactercount:
            charactercount[lowerchar] += 1
        else:
            charactercount[lowerchar] = 1
    return charactercount

def sort_on(items):
    return items["num"]

def dict_to_sorted_list(character_dictionary):
    result_list = []
    for key,value in character_dictionary.items():
        if key.isalpha():
            dictionary = {
                "char": key,
                "num": value
            }
            result_list.append(dictionary)
    result_list.sort(reverse=True, key=sort_on)
    return result_list
