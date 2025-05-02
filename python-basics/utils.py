#!/usr/bin/env python3


def count_vowels(text):
    """
    Parameters
    ----------
    text : str
        Input string to count vowels.

    Returns
    -------
    int
        Number of vowels in the input string text.

    Raises
    ------
    TypeError
        If the type of text is not string.
    """
    if type(text) is not str:
        raise TypeError

    return sum(1 for char in text.lower() if char in "aeiou")


def is_palindrome(text):
    """
    Parameters
    ----------
    text : str
        Input string to check if it is a palindrome.

    Returns
    -------
    bool
        True if text is palindrome, False if not.

    Raises
    ------
    TypeError
        If the type of text is not string.
    """
    if type(text) is not str:
        raise TypeError
    if len(text) == 0:
        return False
    
    text = "".join([char for char in text.lower() if char.isalnum()])

    return text == text[::-1]