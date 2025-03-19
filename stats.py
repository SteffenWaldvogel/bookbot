def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents

def count_words(book_text):
    words = book_text.split()
    word_count = len(words)
    return word_count

def get_characters(book_text):
    lowercase_words = book_text.lower()
    char_counts = {}
    for char in lowercase_words:
        if char in char_counts:
            char_counts[char] +=1
        else:
            char_counts[char] = 1
    return char_counts

def get_sorted_idiot(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({"char": char, "count": count})
    def sort_on(dict):
        return dict["count"]

    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars