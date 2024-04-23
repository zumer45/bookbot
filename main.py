def main():
    file_data = open_file('./books/frankenstein.txt')
    word_count = count_words(file_data)
    letter_count = count_letter(file_data)
    book_report = report(file_data)
    # sorted_dict = sorted_dic(file_data)
    print(book_report)

def open_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    
def count_words(text):
    words = text.split()
    return len(words)

def count_letter(text):
    words = text

    letter_feq = {}

    for letter in words.lower():
        if letter.isalpha():
            if letter in letter_feq:
                letter_feq[letter] += 1
            else: 
                letter_feq[letter] = 1

    return letter_feq

def sorted_dic(text):
    letter_dic = count_letter(text)

    return sorted(letter_dic.items(), key=lambda item: item[1], reverse=True)

def report(text):
    word_count = count_words(text)
    sorted_items = sorted_dic(text)
    print("--- Begin report of books/frankenstein.txt ---")
    print()
    print(f"{word_count} words found in the document")
    print()
    for letter, count in sorted_items:
        print(f"The '{letter}' character was found {count} times")
        print()
    print()
    print("--- End report ---")
    

if __name__ == '__main__':
    main()
