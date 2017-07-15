"""
Write a function that takes in a string and returns
a Boolean -> True if the input string is a palindrome
and False if it is not. An empty string is considered
a palindrome. You also need to account for the space
character. For example, "race car" should return False
as read backward it is "rac ecar".
"""


def is_palindrome(input_string):
    return input_string == input_string[::-1]
