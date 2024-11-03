from itertools import count

import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(values:list[int], start:int) -> Optional[int]:
    if start >= len(values) or start < 0:
        return None

    mindex = start
    for idx in range(start + 1, len(values)):
        if values[idx] < values[mindex]:
            mindex = idx

    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(values:list[int]) -> None:
    for idx in range(len(values) - 1):
        mindex = index_smallest_from(values, idx)
        tmp = values[mindex]
        values[mindex] = values[idx]
        values[idx] = tmp


# Part 1
def selection_sort_books(books: list[data.Book])->list[data.Book]:
    for idx in range(len(books) - 1):
        mindex = idx
        for j in range(idx+1, len(books)):
            if books[j].title.lower() < books[mindex].title.lower():
                mindex = j
        if mindex != idx:
            temp = books[idx]
            books[idx] = books[mindex]
            books[mindex] = temp
    return books

# Part 2
def swap_case(string1: str)->str:
    new_word = ""
    for letter in string1:
        if letter.isalpha():
            if letter.islower():
                new_word += letter.upper()
            else:
                new_word += letter.lower()
        else:
            new_word += letter
    return new_word

# Part 3
def str_translate(string1: str, old: str, new: str)->str:
    new_word = ""
    for letter in string1:
        if letter.lower() == old or letter.upper() == old:
            new_word += new
        else:
            new_word += letter
    return new_word

# Part 4
def histogram(phrase: str):
    phrase = phrase.lower()
    str_list: list[str] = phrase.split()
    word_counts: dict[str, int] = {}

    for word in str_list:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
