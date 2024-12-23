def main():
# word counter
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        word_number = len(words)
    print(word_number)
main()


