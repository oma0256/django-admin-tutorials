import csv
import os

from django.core.management.base import BaseCommand, CommandError

from djangoadmin.apps.user_info.models import UserInfo
from djangoadmin.apps.user_info.utils import generate_user_info_data


class Command(BaseCommand):
    help = 'Populates UserInfo model with data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--entries',
            required=True,
            type=int,
            help='Path to csv file with information on the youtube videos'
        )


    def handle(self, *args, **options):
        for num in range(entries):
            data = generate_user_info_data()
            user_info = UserInfo(**data)
            user_info.save()
            message = f'Added {user_info.username} info to database'
            self.stdout.write(self.style.SUCCESS(message))
