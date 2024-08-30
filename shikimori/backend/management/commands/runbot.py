from django.core.management import BaseCommand
from telegram.shikimori_bot.app import run_bot


class Command(BaseCommand):
    help = "starting report bot"

    def handle(self, *args, **options):
        run_bot()