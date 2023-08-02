def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = number_of_words(text)
    word_frequency = string_words(text)

    ending_report(word_count, word_frequency)

def get_book_text(path):
    with open(path) as f:
        return f.read()

def number_of_words(text):
    words = text.split()
    count = len(words)
    return count

def string_words(text):
    lower_words = text.lower()  # Convert text to lowercase and split into words
    string_dict = {}
    for word in lower_words:
        if word in string_dict:
            string_dict[word] += 1
        else:
            string_dict[word] = 1
    return string_dict

def ending_report(word_count, word_frequency):
    print("--- Begin report of books/frankenstein.txt ---")
    print("Number of words:", word_count)
    for word, count in word_frequency.items():
        clean_word = ''.join(char for char in word if char.isalpha())
        if clean_word:
            print(f"The word '{clean_word}' was found {count} times")
    print("--- End report ---")

main()
