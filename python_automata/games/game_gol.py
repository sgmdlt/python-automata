from python_automata.io import get_x, get_y

ALIVE_CONDITION = (2, 3)
NEWBORN_CONDITION = 3
NEIBOR_DELTAS = (  # noqa: WPS317 FIX INDENTATION
    (-1, -1), (-1, 0), (-1, 1), (0, -1),  # noqa: WPS221 Jones Complexity
    (0, 1), (1, -1), (1, 0), (1, 1),
)


def game(live_cells, generation):  # noqa: WPS231

    for _ in range(generation):

        next_gen_cells = set()

        for cell in live_cells:
            if is_alive_cell(cell, live_cells):
                next_gen_cells.add(cell)

            neibors = get_neibors(cell)
            for neibor in neibors:
                if is_newborn(neibor, live_cells):
                    next_gen_cells.add(neibor)

        live_cells = next_gen_cells
    return live_cells


def is_alive_cell(cell, live_cells):
    return check_population(cell, live_cells) in ALIVE_CONDITION


def is_newborn(cell, live_cells):
    return check_population(cell, live_cells) == NEWBORN_CONDITION


def check_population(cell, live_cells):
    neibors = get_neibors(cell)
    return sum(1 for n in neibors if n in live_cells)


def get_neibors(cell):
    cell_x, cell_y = get_x(cell), get_y(cell)
    deltas = ((get_x(d), get_y(d)) for d in NEIBOR_DELTAS)
    return ((cell_x + dx, cell_y + dy) for dx, dy in deltas)
