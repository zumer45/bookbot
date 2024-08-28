
def main():
    book_path = "./books/frankenstein.txt"
    file_contents = get_book_text(book_path)
    word_count = count_words_in_text(file_contents)
    char_count = count_chars_in_text(file_contents)
    final_report(file_contents)
    
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

def final_report(text):
    word_count = count_words_in_text(text)
    char_dict = count_chars_in_text(text)
    sorted_dict = sorted(char_dict.items(), key=lambda item: item[1], reverse=True)

    print("--- Begin report of books/frankenstein.txt ---")
    print("\n")
    print(f"{word_count} words found in the document")
    print("\n")
    
    

    for i , j in sorted_dict:
        print(f"The {i} character was found {j} times")
    print("--- End report ---")
    

           



main()