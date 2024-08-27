from django.db import models
from backend.models.base import TimeBasedModel
from telegram.models import TelegramUser

class Account(TimeBasedModel):
    class Sex(models.TextChoices):
        MALE = 'М', 'Муж.'
        FEMALE = 'Ж', "Жен."
        UNDEFINED = 'Н', 'Не указано'

    sex = models.CharField("Пол", max_length=1, choices=Sex.choices, default=Sex.UNDEFINED)
    birthday = models.DateField("Дата рождения")
    show_age = models.BooleanField("Показать возраст", default=False)
    show_adult = models.BooleanField("Показать 18+ контент", default=False)
    avatar = models.ImageField("Аватар", upload_to="users/avatar", blank=True)
    about = models.TextField("О себе", max_length=1024, blank=True, null=True)
    tg_user = models.ForeignKey(TelegramUser, on_delete=models.SET_NULL, null=True, blank=True)

