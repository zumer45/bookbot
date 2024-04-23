def main():
    file_data = open_file('./books/frankenstein.txt')
    print(file_data)

def open_file(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents
    

if __name__ == '__main__':
    main()
