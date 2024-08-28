
def main():
    book_path = "./books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words_in_text(file_contents)
    char_count = count_chars_in_text(file_contents)
    print(char_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_text(text):
    words = text.split()
    return len(words)

def count_chars_in_text(text):
    char_dict = {}
    for word in text:
        for char in word.lower(): 
            if char in char_dict and char.isalpha():
                char_dict[char] += 1
            elif char not in char_dict and char.isalpha():
                char_dict[char] = 1
        

    return char_dict
           



main()