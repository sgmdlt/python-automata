def get_x(cell):
    return cell[0]


def get_y(cell):
    return cell[1]


def read(board):  # noqa: WPS210 it's ok to have many variables
    live_cells = set()
    rows = len(board)
    cols = len(board[0])
    for y in range(0, rows):
        for x in range(0, cols):
            if board[y][x] == 1:
                cell = (x, y)
                live_cells.add(cell)
    return live_cells


def output(live_cells):  # noqa: WPS210 it's ok to have many variables
    col = [get_x(cell) for cell in live_cells]
    row = [get_y(cell) for cell in live_cells]
    board = []

    for y in range(min(row), max(row) + 1):
        line = []
        for x in range(min(col), max(col) + 1):
            cell = (x, y)
            if cell in live_cells:
                symbol = 1
            else:
                symbol = 0
            line.append(symbol)
        board.append(line)
    return board
