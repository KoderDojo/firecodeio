"""
Write a function that takes in a list of ints and uses
the Bubble Sort algorithm to sort the list 'in place'
in ascending order. The method should return the same,
in-place sorted list. Note: Bubble sort is one of the
most inefficient ways to sort a large list of integers.
Nevertheless, it is an interview favorite. Bubble sort
has a time complexity of O(n2). However, if the sample
size is small, bubble sort provides a simple
implementation of a classic sorting algorithm.
"""


def bubble_sort(a_list):
    if a_list is None or len(a_list) < 2:
        return a_list

    for i in range(len(a_list) - 1, 0, -1):

        swap = False
        for j in range(0, i):
            if a_list[j] > a_list[j+1]:
                a_list[j], a_list[j+1] = a_list[j+1], a_list[j]
                swap = True

        if not swap:
            break

    return a_list
