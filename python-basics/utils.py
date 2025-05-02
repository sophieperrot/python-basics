#!/usr/bin/env python3


def count_vowels(text):
    """
    Parameters
    ----------
    text : str

    Returns
    -------
    int
        Number of vowels in the input string text
    """
    if type(text) != str:
        raise TypeError

    return sum(1 for char in text.lower() if char in "aeiou")


def is_palindrome(text):
    """
    Parameters
    ----------
    text : str

    Returns
    -------
    bool
        True if text is palindrome, False if not
    """
    if type(text) != str:
        raise TypeError
    if len(text) == 0:
        return False
    
    text = "".join([char for char in text.lower() if char.isalnum()])

    return text == text[::-1]