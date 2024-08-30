from aiogram import types, Router, filters
from aiogram.fsm.context import FSMContext
from telegram.services import telegram_user as tus
from telegram.shikimori_bot.utils.text import get_text
from telegram.shikimori_bot.data import text_data as td
from telegram.shikimori_bot.data.dataclasses import MessageData
from telegram.shikimori_bot.keyboards import inline as ik
from telegram.shikimori_bot.utils import message_worker as mw


commands = Router()

@commands.message(filters.CommandStart())
async def start_message(message: types.Message, state: FSMContext):
    telegram_id = message.from_user.id
    user = await tus.get_user_by_id(telegram_id=telegram_id) or await tus.create_telegram_user(
        name= message.from_user.full_name,
        telegram_id= telegram_id,
        username= message.from_user.username,        
    )
    lang = user.selected_language
    text = await get_text(key=td.START_MESSAGE, lang=lang)
    keyboard = await ik.main_keyboard(lang=lang)
    md = MessageData(
        message=message,
        state=state,
        text=text,
        keyboard=keyboard,
        delete_income_message=True
    )
    await mw.try_edit_main_message(
        md=md
    )
    

