def get_words():
    return ["this", "is", "simple", "list"]


def print_words(words):
    for word in words:
        print(word)

def main():
    words = get_words()
    print_words(words)
    
if __name__ == '__main__':
    main()