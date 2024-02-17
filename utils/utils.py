from random import choice

from lexicon.lexicon import LEXICON_RU


def get_random_figure() -> str:
    figure = choice(list(LEXICON_RU['button_texts']['figures'].values()))
    return figure


def get_game_result(user_figure: str, bot_figure: str) -> str:
    if user_figure == bot_figure:
        return 'draw'

    if user_figure == 'Бумага' and bot_figure == 'Камень':
        return 'win'
    elif user_figure == 'Ножницы' and bot_figure == 'Бумага':
        return 'win'
    elif user_figure == 'Камень' and bot_figure == 'Ножницы':
        return 'win'
    else:
        return 'loose'
