"""
The classic minesweeper game.
Pass in  a list of lists with
'*' for the mines, like below
minefield = ["   ", " * ", "   "]
should return a count in each neighboring space
for all adjacent spots touching a mine
like so ['111', '1*1', '111']
"""

def annotate(minefield):
    if any(len(row) != len(minefield[0]) for row in minefield):
        raise ValueError("The board is invalid with current input.")

    valid_chars = {' ', '*'}
    for row in minefield:
        for char in row:
            if char not in valid_chars:
                raise ValueError("The board is invalid with current input.")

    for current_row in range(len(minefield)):
        for current_col in range(len(minefield[0])):

            cell = minefield[current_row][current_col]
            if cell == "*":
                continue
            neighbors = []
            directions = [
                (-1, -1),
                (-1, 0),
                (-1, 1),
                (0, -1),
                (0, 1),
                (1, -1),
                (1, 0),
                (1, 1),
            ]
            for drow, dcol in directions:
                r, c = current_row + drow, current_col + dcol
                if 0 <= r < len(minefield) and 0 <= c < len(minefield[0]):
                    neighbors.append((r, c))
            count_mines = 0
            for r, c in neighbors:
                if minefield[r][c] == "*":
                    count_mines += 1
            if count_mines > 0:
                list_row = list(minefield[current_row])
                list_row[current_col] = str(count_mines)
                minefield[current_row] = "".join(list_row)

    return minefield
