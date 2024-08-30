from telegram.models import TelegramUser
from text_data.services import text as txt

async def create_telegram_user(name:str, telegram_id:int, username:str = None):
    language = await txt.get_default_language()
    return await TelegramUser.objects.acreate(
        name=name,
        telegram_id=telegram_id,
        username=username,
        selected_language=language,
    )


async def get_all_users():
    return TelegramUser.objects.all()

async def get_user_by_id(telegram_id: int):
    return await TelegramUser.objects.filter(telegram_id=telegram_id).afirst()
    