"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).

    >>> lower_bound([1, 4, 7, 9, 20, 24, 697], 20)
    4

    """
    start = 0 # start of search interval
    end = len(x) # end of search interval
    middel = start + ((end - start)//2) # middel of search interval

    while (end-start) >= 1 and middel < len(x):
        if x[middel] > v:
            end = middel # new interval is cut in half
            middel = start + ((end - start)//2) # middel of new interval is found
        if x[middel] < v:
            start = middel + 1 # new interval is cut in half, +1 because python is start inclusive
            middel = start + ((end - start)//2)
        if x[middel] == v:
            return middel
    else:
        return len(x)


def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).

    >>> upper_bound([1, 4, 7, 9, 20, 24, 697], 20)
    4

    """
    start = 0 # start of search interval
    end = len(x) # end of search interval
    middel = start + ((end - start)//2) # middel of search interval

    while (end-start) >= 1 and middel < len(x):
        if x[middel] > v:
            end = middel # new interval is cut in half
            middel = start + ((end - start)//2) # middel of new interval is found
        if x[middel] < v:
            start = middel + 1 # new interval is cut in half, +1 because python is start inclusive
            middel = start + ((end - start)//2)
        if x[middel] == v:
            return middel
    else:
        return len(x)
