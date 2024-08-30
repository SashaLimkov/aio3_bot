from text_data.models import Text, Language, Translate


async def get_text_by_language_and_key(lang: Language, key: str) -> str:
    if key is None:
        return "Нет текста"
    text_key = await Text.objects.filter(key=key).afirst()
    res = await Translate.objects.filter(text_key=text_key, language=lang).afirst()
    return res.translate


async def get_key_by_text(text: str):
    return Translate.objects.filter(translate=text).afirst().text_key.key


async def get_translate_by_text(text: str) -> Translate:
    pass


async def get_default_language():
    return await Language.objects.afirst()


async def get_all_languages():
    return Language.objects.all()


async def get_language_by_name(lang_name: str) -> Language:
    return Language.objects.filter(name=lang_name).afirst()