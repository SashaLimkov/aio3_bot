from text_data.models import Language
from text_data.services.text import get_text_by_language_and_key


async def get_text(key: str, lang: Language) -> str:
    return await get_text_by_language_and_key(key=key, lang=lang)