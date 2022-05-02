import pytest

from python_automata.scripts.run import main


INPUT = [
    [1,0,0],
    [1,1,1],
    [1,0,0],
]

OUTPUT_GOL = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 0, 0, 1],
    [0, 1, 0, 1, 0],
    [0, 0, 1, 0, 0],
]

OUTPUT_ROT = [
    [1,0,0],
    [1,1,1],
    [1,0,0],
]


GAMES = {
    'game_of_life': ('gol',INPUT, 6, OUTPUT_GOL),
    'rotate_automata': ('rot', INPUT, 428, OUTPUT_ROT),
}

@pytest.mark.parametrize(
    'game, input, generations, output', 
    GAMES.values(),
    ids=GAMES.keys()
)
def test_games(game, input, generations, output):
    assert main(input, generations, name=game) == output


def test_wrong_game():
    with pytest.raises(RuntimeError, match=r'game'):
        main(INPUT, 10, name='game_of_thrones')
