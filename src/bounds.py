"""
Module for experimenting with lower and upper bounds.

Unlike in the BED functionality, where we need to search for a lower bound in
a list of features, here we only concern ourselves with lists of integers.
"""


def lower_bound(x: list[int], v: int) -> int:
    """Get the index of the lower bound of v in x.

    If all values in x are smaller than v, return len(x).

    >>> lower_bound([4, 4, 7, 7, 9, 10, 20, 20, 20], 20)
    6

    >>> lowe_bound([1, 2, 5], 10)
    3

    """
    start = 0 # start of search interval
    end = len(x) # end of search interval
    middel = start + ((end - start)//2) # middel of search interval

    while start < end:
        middel = start + ((end - start)//2) # middel of interval
        if x[middel] >= v:
            end = middel + 1
        else:
            start = middel
    return middel

# Previous verison did not work as I intended,
# got inspiration from https://www.youtube.com/watch?v=6-15eccc6ek&ab_channel=CodeSavant

def upper_bound(x: list[int], v: int) -> int:
    """Get the index of the upper bound of v in x.

    If all values in x are smaller than v, return len(x).

    >>> upper_bound([4, 4, 7, 7, 9, 10, 20, 20, 20], 7)
    3

    >>> upper_bound([1, 2, 5], 10)
    3

    """
    start = 0 # start of search interval
    end = len(x) # end of search interval
    middel = start + ((end - start)//2) # middel of search interval

    while start < end:
        middel = start + ((end - start)//2) # middel of interval
        if x[middel] <= v:
            start = middel + 1
        else:
            end = middel
    return middel
