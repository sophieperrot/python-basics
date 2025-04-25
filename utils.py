#!/usr/bin/env python3

import re


def num_vowels(text: str):
    if type(text) != str:
        raise TypeError
    vowels = re.findall("[aeiou]", text)
    return len(vowels)


def is_palindrome(text):
    if type(text) != str:
        raise TypeError
    if len(text) == 0:
        return False
    
    text = text.replace(" ", "")
    text = text.lower()
    text_length = len(text)

    first_half = text[:text_length//2]
    if text_length % 2 == 0:
        second_half = text[text_length//2:]
    else:
        second_half = text[text_length//2+1:]
    if first_half == second_half[::-1]:
        return True
    return False