
def main():
    book_path = "./books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words_in_text(file_contents)
    print(word_count)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words_in_text(text):
    words = text.split()
    return len(words)

main()