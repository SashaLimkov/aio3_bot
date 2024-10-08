# Generated by Django 5.1 on 2024-08-27 00:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "sex",
                    models.CharField(
                        choices=[("М", "Муж."), ("Ж", "Жен."), ("Н", "Не указано")],
                        default="Н",
                        max_length=1,
                        verbose_name="Пол",
                    ),
                ),
                ("birthday", models.DateField(verbose_name="Дата рождения")),
                (
                    "show_age",
                    models.BooleanField(default=False, verbose_name="Показать возраст"),
                ),
                (
                    "show_adult",
                    models.BooleanField(
                        default=False, verbose_name="Показать 18+ контент"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True, upload_to="users/avatar", verbose_name="Аватар"
                    ),
                ),
                (
                    "about",
                    models.TextField(
                        blank=True, max_length=1024, null=True, verbose_name="О себе"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Genre",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                ("name", models.CharField(max_length=100)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Anime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                ("name", models.CharField(max_length=100)),
                ("image", models.ImageField(upload_to="anime")),
                ("episodes", models.IntegerField()),
                (
                    "rating",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("G", "G"),
                            ("PG", "PG"),
                            ("PG-13", "PG-13"),
                            ("R-17", "R-17"),
                            ("R+", "R+"),
                            ("Rx", "Rx"),
                        ],
                        default=None,
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "anime_rating",
                    models.FloatField(blank=True, default=None, null=True),
                ),
                ("genres", models.ManyToManyField(to="backend.genre")),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="UserAnime",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="Создано"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, verbose_name="Обновлено"),
                ),
                (
                    "status",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Смотрю", "Смотрю"),
                            ("Просмотрено", "Просмотрено"),
                            ("Брошено", "Брошено"),
                            ("Запланировано", "Запланировано"),
                        ],
                        default=None,
                        max_length=100,
                        null=True,
                    ),
                ),
                ("user_rate", models.FloatField(blank=True, default=None, null=True)),
                (
                    "anime",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="backend.anime"
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="backend.account",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
