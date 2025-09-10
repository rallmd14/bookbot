from stats import word_counting_text
from stats import character_counting_text
from stats import sorting_dictionaries
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) == 1:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    frankenstein_text = get_book_text(book_path)
    word_count = word_counting_text(frankenstein_text)
    character_dictionary = character_counting_text(frankenstein_text)
    sorted_dictionary = sorting_dictionaries(character_dictionary)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_dictionary:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")

main()
