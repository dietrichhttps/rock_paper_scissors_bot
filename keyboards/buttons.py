from aiogram.types import KeyboardButton

from lexicon.lexicon import LEXICON_RU

yes_btn = KeyboardButton(text=LEXICON_RU['button_texts']['start']['yes'])
no_btn = KeyboardButton(text=LEXICON_RU['button_texts']['start']['no'])

rock_btn = KeyboardButton(text=LEXICON_RU['button_texts']['figures']['rock'])
paper_btn = KeyboardButton(text=LEXICON_RU['button_texts']['figures']['paper'])
scissors_btn = KeyboardButton(text=LEXICON_RU['button_texts']['figures']['scissors'])
