import os

from typing import Dict

from .lexicon_methods import get_text

LEXICON_DIR = os.path.dirname(os.path.abspath(__file__))

LEXICON_RU = {
    'chat_texts': {
        'start_question': {
            '/start': get_text(LEXICON_DIR, 'ru/chat_texts/start_question/start.txt'),
        },
        'start_answers': {
            'if_yes': get_text(LEXICON_DIR, 'ru/chat_texts/start_answers/if_yes.txt'),
            'if_no': get_text(LEXICON_DIR, 'ru/chat_texts/start_answers/if_no.txt'),
        },
        'game_results': {
            'win': get_text(LEXICON_DIR, 'ru/chat_texts/game_results/win.txt'),
            'loose': get_text(LEXICON_DIR, 'ru/chat_texts/game_results/loose.txt'),
            'draw': get_text(LEXICON_DIR, 'ru/chat_texts/game_results/draw.txt'),
            'try_again': get_text(LEXICON_DIR, 'ru/chat_texts/game_results/try_again.txt')
        },
    },
    'button_texts': {
        'start': {
            'yes': get_text(LEXICON_DIR, 'ru/button_texts/start/yes.txt'),
            'no': get_text(LEXICON_DIR, 'ru/button_texts/start/no.txt'),
        },
        'figures': {
            'rock': get_text(LEXICON_DIR, 'ru/button_texts/figures/rock.txt'),
            'paper': get_text(LEXICON_DIR, 'ru/button_texts/figures/paper.txt'),
            'scissors': get_text(LEXICON_DIR, 'ru/button_texts/figures/scissors.txt'),
        }
    }
}
