#!/usr/bin/env python3
"""This is a simple module doing simple word listing.
By the way this is how you add documentation to your module
"""

def get_words():
    """This function will retun a list of word.
    By the way this is how you add documentation to your functions

    Args:
        None
    Return:
        List of words
    """
    return ["this", "is", "simple", "list"]


def print_words(words):
    """This function will print a list of word.

    Args:
        List of words
    Return:
        None
    """
    for word in words:
        print(word)

def main():
    """This is a test main function.

    Args:
        None
    Return:
        None
    """

    words = get_words()
    print_words(words)
    
if __name__ == '__main__':
    main()