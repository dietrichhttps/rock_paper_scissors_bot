from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import ReplyKeyboardMarkup

from .buttons import yes_btn, no_btn
from .buttons import rock_btn, paper_btn, scissors_btn

# Инициализировал билдеры
yes_or_no_kb_builder = ReplyKeyboardBuilder()
rock_paper_scissors_kb_builder = ReplyKeyboardBuilder()

# Добавил кнопки в билдеры
yes_or_no_kb_builder.row(yes_btn, no_btn, width=2)
rock_paper_scissors_kb_builder.row(
    rock_btn, paper_btn, scissors_btn,
    width=3
)

# Создал объект клавиатуры "Да/Нет"
yes_or_no_keyboard: ReplyKeyboardMarkup = yes_or_no_kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)

# Создал объект клавиатуры "Камень ножницы бумага"
rock_paper_scissors_keyboard: ReplyKeyboardMarkup = rock_paper_scissors_kb_builder.as_markup(
    resize_keyboard=True,
    one_time_keyboard=True
)
