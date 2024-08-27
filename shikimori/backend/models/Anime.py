from backend.models.base import TimeBasedModel
from django.db import models
from backend.models.User import Account

class Genre(TimeBasedModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Anime(TimeBasedModel):
    class Rating(models.TextChoices):
        G = "G", "G"
        PG = "PG", "PG"
        PG_13 = "PG-13", "PG-13"
        R_17 = "R-17", "R-17"
        R_plus = "R+", "R+"
        Rx = "Rx", "Rx"

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='anime')
    episodes = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    rating = models.CharField(max_length=10, choices=Rating.choices, default=None, null=True, blank=True)
    anime_rating = models.FloatField(null=True, blank=True, default=None)


class UserAnime(TimeBasedModel):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)
    
    class Status(models.TextChoices):
        WATCHING = 'Смотрю', "Смотрю"
        WATCHED = "Просмотрено",  "Просмотрено"
        DROPED = "Брошено", "Брошено"
        PLANNED = "Запланировано", "Запланировано"
    
    status = models.CharField(max_length=100, choices=Status.choices, default=None, null=True, blank=True)
    user_rate = models.FloatField(null=True, blank=True, default=None)