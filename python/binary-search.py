"""
Write binary search.
"""


def binary_search(a_list, item):
    if a_list is None or len(a_list) == 0:
        return False

    lo, hi = 0, len(a_list) - 1

    while lo <= hi:
        mid = (lo + hi) // 2

        if a_list[mid] == item:
            return True

        if a_list[mid] < item:
            lo = mid + 1
        else:
            hi = mid - 1

    return False
