from aiogram import types
from aiogram.fsm.context import FSMContext
from telegram.shikimori_bot.data.dataclasses import MessageData
import logging
from aiogram.exceptions import TelegramBadRequest
from telegram.shikimori_bot.config.loader import bot

async def try_send_message(md: MessageData): 
    try:
        mes = await md.message.answer(
            text=md.text,
            reply_markup=md.keyboard
        )
        if md.main_message:
            await md.state.update_data(
                {
                    "main_message_id": mes.message_id
                }
            )
        if md.delete_income_message:
            await md.message.delete()

    except Exception as e:
        logging.exception(e)


async def try_edit_main_message(md:MessageData):
    data = await md.state.get_data()
    try:
        await bot.edit_message_text(
            text=md.text,
            reply_markup=md.keyboard,
            chat_id=md.message.from_user.id,
            message_id=data.get("main_message_id")
        )
    except TelegramBadRequest:
        await delete_message(
            chat_id=md.message.from_user.id,
            message_id=data.get("main_message_id")
        )
        await try_send_message(md=md)



async def delete_message(message_id:FSMContext, chat_id:int):
    await bot.delete_message(
        chat_id=chat_id,
        message_id=message_id
    )