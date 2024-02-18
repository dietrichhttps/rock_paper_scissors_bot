from aiogram.types import KeyboardButton

from lexicon.lexicon import LEXICON_RU

# Кнопки да и нет
yes_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['button_texts']['start']['yes'])
no_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['button_texts']['start']['no'])

# Кнопки камень ножницы бумага
rock_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['button_texts']['figures']['rock'])
paper_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['button_texts']['figures']['paper'])
scissors_btn: KeyboardButton = KeyboardButton(
    text=LEXICON_RU['button_texts']['figures']['scissors'])
