import os
from django.core.management.base import BaseCommand
from documentation import app_settings


class Command(BaseCommand):
    help = "Compiles documentation"
    args = ''

    def handle(self, *labels, **options):
        current_path = os.getcwd()
        os.chdir(app_settings.DOCUMENTATION_ROOT)
        print os.getcwd()
        os.system("make html")
        os.chdir(current_path)
