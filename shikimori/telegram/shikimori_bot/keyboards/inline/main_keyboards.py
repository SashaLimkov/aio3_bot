from aiogram import types
from aiogram.utils.keyboard import InlineKeyboardBuilder
from text_data.models import Language
from telegram.shikimori_bot.data import text_data as td
from telegram.shikimori_bot.utils.text import get_text

__all__ = [
    'main_keyboard',
    ]

async def main_keyboard(lang: Language):
    keyboard = InlineKeyboardBuilder()
    keyboard.button(
        text= await get_text(key=td.KB_EDIT_MESSAGE, lang=lang),
        callback_data= td.KB_EDIT_MESSAGE,
    )
    return keyboard.as_markup()