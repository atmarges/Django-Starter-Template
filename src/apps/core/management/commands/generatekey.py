from django.core.management.base import BaseCommand
from django.core.management.utils import get_random_secret_key
from pathlib import Path
import re


class Command(BaseCommand):
    help = "Generate a new secret key for the django project"

    def handle(self, *args, **kwargs):
        secret_key = 'SECRET_KEY = ' + get_random_secret_key()
        settings_file = next(Path().rglob('*/settings.py'))

        with open(settings_file, mode='r') as f:
            filedata = f.read()

        regex = r'(?<=SECRET_KEY \=\s\').*(?=\')'
        secret_key = re.findall(regex, filedata)[0]

        filedata = filedata.replace(secret_key, get_random_secret_key())

        with open(settings_file, mode='w') as f:
            f.write(filedata)

        message = "New django secret key generated successfully."
        self.stdout.write(self.style.SUCCESS(message))
