import numpy as np

def np_diamond(letter):
    """
    Create a diamond, with the chosen letter as the mid point on the outer edges.
    'A' should make up the first and last points on the diamond.
    """
    letters = [chr(i) for i in range(ord('A'), ord(letter)+1)]

    n = len(letters)
    size = 2 * n - 1

    array = np.full((size, size), ' ', dtype=str)
    # If we don't have numpy, like the website exercise use the below array
    # array = [[' ' for _ in range(size)] for _ in range(size)]

    mid = n - 1

    for i, char in enumerate(letters):
        row =  i

        col_left = mid - i
        col_right = mid + i

        array[row, col_left] = char
        array[row, col_right] = char

        array[size - row - 1, col_left] = char
        array[size - row - 1, col_right] = char

    # diamond = '\n'.join(''.join(row) for row in array)
    diamond = [''.join(row) for row in array]
    return diamond
