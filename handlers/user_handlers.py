from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command

from lexicon.lexicon import LEXICON_RU

from keyboards.keyboards import yes_or_no_keyboard, rock_paper_scissors_keyboard

from utils.utils import get_random_figure, get_game_result

router = Router()


@router.message(Command(commands=['start', '/start@pepis_bepis_bot']))
async def process_start_command(message: Message):
    await message.answer(
        text=LEXICON_RU['chat_texts']['start_question']['/start'],
        reply_markup=yes_or_no_keyboard
        )


@router.message(F.text == LEXICON_RU['button_texts']['start']['no'])
async def process_no_answer(message: Message):
    await message.answer(text=LEXICON_RU['chat_texts']['start_answers']['if_no'])


@router.message(F.text == LEXICON_RU['button_texts']['start']['yes'])
async def process_yes_answer(message: Message):
    await message.answer(
        text=LEXICON_RU['chat_texts']['start_answers']['if_yes'],
        reply_markup=rock_paper_scissors_keyboard
    )


@router.message(F.text == LEXICON_RU['button_texts']['figures']['rock'])
async def process_rock_answer(message: Message):
    await process_game_answer(message, LEXICON_RU['button_texts']['figures']['rock'])


@router.message(F.text == LEXICON_RU['button_texts']['figures']['paper'])
async def process_paper_answer(message: Message):
    await process_game_answer(message, LEXICON_RU['button_texts']['figures']['paper'])


@router.message(F.text == LEXICON_RU['button_texts']['figures']['scissors'])
async def process_scissors_answer(message: Message):
    await process_game_answer(message, LEXICON_RU['button_texts']['figures']['scissors'])


async def process_game_answer(message: Message, figure: str):
    bot_figure = get_random_figure()
    game_result = get_game_result(figure, bot_figure)

    try:
        await message.answer(text=bot_figure)

        if game_result == 'win':
            await message.answer(text=LEXICON_RU['chat_texts']['game_results']['win'])
        elif game_result == 'loose':
            await message.answer(text=LEXICON_RU['chat_texts']['game_results']['loose'])
        elif game_result == 'draw':
            await message.answer(text=LEXICON_RU['chat_texts']['game_results']['draw'])
    finally:
        await message.answer(
            text=LEXICON_RU['chat_texts']['game_results']['try_again'],
            reply_markup=yes_or_no_keyboard
            )