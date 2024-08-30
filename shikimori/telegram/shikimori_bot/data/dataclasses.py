from dataclasses import dataclass
from aiogram import types
from aiogram.fsm.context import FSMContext

@dataclass
class MessageData:
    message: types.Message
    state: FSMContext
    text: str
    keyboard: types.InlineKeyboardMarkup | types.ReplyKeyboardMarkup | None
    main_message: bool = True
    file: types.InputFile = None
    delete_income_message: bool = False
