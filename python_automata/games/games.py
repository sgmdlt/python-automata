from python_automata.games.game_gol import game as gol
from python_automata.games.game_rot import game as rot

GAMES = {  # noqa: WPS407
    'gol': gol,
    'rot': rot,
}


def select_game(name):
    try:
        game = GAMES[name]
    except KeyError:
        message = 'Wrong game {n}. Choose game from list: {g}'.format
        raise RuntimeError(message(n=name, g=GAMES))
    return game
