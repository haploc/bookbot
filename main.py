import sys
from stats import count_words, count_characters, dict_to_sorted_list

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book = sys.argv[1]
        file_contents = get_book_text(book)
        num_words = count_words(file_contents)
        char_count = count_characters(file_contents)
        char_count_sorted_list = dict_to_sorted_list(char_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for char_count_dict in char_count_sorted_list:
            character = char_count_dict["char"]
            number = char_count_dict["num"]
            print(f"{character}: {number}")
        print("============= END ===============")

main()
