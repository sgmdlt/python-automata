from itertools import cycle

from python_automata.io import get_x, get_y

START_POINT = ((1, 1), (0, 0))
BLOCK_SIZE = 2


def game(live_cells, generations):  # noqa: WPS210 too many variables
    start_point = cycle(START_POINT)

    for _ in range(generations):
        next_gen_cells = set()

        blocks = get_blocks(live_cells, next(start_point))
        for block_start, cells in blocks.items():
            next_gen_cells.update(transform(block_start, cells))

        live_cells = next_gen_cells
    return live_cells


def get_blocks(live_cells, start_point):
    blocks = {}

    for cell in live_cells:
        dist = (
            (get_x(cell) - get_x(start_point)) // BLOCK_SIZE,
            (get_y(cell) - get_y(start_point)) // BLOCK_SIZE,
        )

        block_start = (
            get_x(dist) * BLOCK_SIZE + get_x(start_point),
            get_y(dist) * BLOCK_SIZE + get_y(start_point),
        )
        cell_list = blocks.setdefault(block_start, set())
        cell_list.add(cell)
    return blocks


def transform(block_start, cells):  # noqa: WPS210
    rule = {
        'rotation': {
            (0, 0): (1, 0),
            (1, 0): (1, 1),
            (1, 1): (0, 1),
            (0, 1): (0, 0),
        },
        'count': 1,
    }

    block_x, block_y = get_x(block_start), get_y(block_start)
    new_positions = set()

    if len(cells) == rule['count']:
        for cell in cells:
            pos = (get_x(cell) - block_x, get_y(cell) - block_y)
            new_positions.add(rule['rotation'].get(pos))

        return {
            (get_x(p) + block_x, + get_y(p) + block_y)
            for p in new_positions
        }

    return cells
