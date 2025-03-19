import sys
from stats import count_words, get_book_text, get_characters, get_sorted_idiot

def main(): 
    #checking if they input a file
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_text = get_book_text(sys.argv[1])
    num_words = count_words(book_text)
    chars = get_characters(book_text)
    sorted_chars = get_sorted_idiot(get_characters(book_text))
    
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char_dict in sorted_chars:
        char = char_dict["char"]
        count = char_dict["count"]
        print(f"{char}: {count}")
    print("============= END ===============")

main()