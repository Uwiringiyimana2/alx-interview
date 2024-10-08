#!/usr/bin/python3
"""selection sort"""


def findsmallestnumb(arr):
    """ find the smallest number in array
    """
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionsort(arr):
    """ sort from smallest to the biggest number
    """
    new = []
    for i in range(len(arr)):
        sm = findsmallestnumb(arr)
        new.append(arr.pop(sm))
    return new


if __name__ == "__main__":
    print(selectionsort([5, 3, 6, 2, 10]))
