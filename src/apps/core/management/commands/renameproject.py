from django.core.management.base import BaseCommand
from pathlib import Path
import os
import re


class Command(BaseCommand):
    help = "Rename django project"

    def get_project_name(self, settings_path='*/settings.py'):
        settings_file = next(Path().rglob(settings_path))

        with open(settings_file, 'r') as f:
            filedata = f.read()

        regex = r'(?<=ROOT_URLCONF \=\s\').*(?=\.urls\')'
        project_name = re.findall(regex, filedata)[0]

        return project_name

    def add_arguments(self, parser):
        parser.add_argument('new_project_name', type=str,
                            help="The new django project name")

    def handle(self, *args, **kwargs):
        current_project_name = self.get_project_name()
        new_project_name = kwargs['new_project_name']

        files_to_rename = [
            current_project_name + '/settings.py',
            current_project_name + '/wsgi.py',
            'manage.py'
        ]

        for file in files_to_rename:
            with open(file, 'r') as f:
                filedata = f.read()

            filedata = filedata.replace(current_project_name, new_project_name)

            with open(file, 'w') as f:
                f.write(filedata)

        os.rename(current_project_name, new_project_name)

        message = "Project has been renamed to " + new_project_name
        self.stdout.write(self.style.SUCCESS(message))
