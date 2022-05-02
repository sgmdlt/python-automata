from python_automata.games.games import select_game
from python_automata.io import output, read

DEFAULT_GAME = 'gol'


def main(source, generations, name=DEFAULT_GAME):
    game = select_game(name)
    cells = read(source)
    new_cells = game(cells, generations)
    return output(new_cells)


if __name__ == '__main__':
    main()
