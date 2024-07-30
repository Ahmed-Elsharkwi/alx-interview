#!/usr/bin/python3
""" perimeter documented """


def island_perimeter(grid):
    """ calculate the perimeter of a specific shape """
    perimeter = 0

    num_rows = len(grid)
    num_columns = len(grid[0])
    for row in range(0, num_rows):
        for column in range(0, num_columns):
            if grid[row][column] == 1:
                if row - 1 >= 0 and grid[row - 1][column] == 0:
                    perimeter += 1

                if row + 1 != num_rows and grid[row + 1][column] == 0:
                    perimeter += 1

                if column - 1 >= 0 and grid[row][column - 1] == 0:
                    perimeter += 1

                if column + 1 != num_columns and grid[row][column + 1] == 0:
                    perimeter += 1
    return perimeter
