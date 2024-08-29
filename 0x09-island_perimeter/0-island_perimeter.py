#!/usr/bin/python3
""" Finding a perimeter of island
"""


def island_perimeter(grid):
    """ Finding a perimeter of island
    """
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col]:
                perimeter += 4
                if row > 0 and grid[row - 1][col]:
                    perimeter -= 2
                if col > 0 and grid[row][col - 1]:
                    perimeter -= 2
    return perimeter
