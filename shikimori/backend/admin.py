from django.contrib import admin
from backend.models import Account, Anime, Genre, UserAnime

admin.site.register(Account)
admin.site.register(Anime)
admin.site.register(Genre)
admin.site.register(UserAnime)