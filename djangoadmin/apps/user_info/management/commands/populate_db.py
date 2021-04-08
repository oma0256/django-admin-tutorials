import os

from django.core.management.base import BaseCommand

from djangoadmin.apps.user_info.models import UserInfo
from djangoadmin.apps.user_info.utils import generate_user_info_data


class Command(BaseCommand):
    help = 'Populates UserInfo model with data'

    def add_arguments(self, parser):
        parser.add_argument(
            '--instances',
            required=True,
            type=int,
            help='Number of UserInfo instances to create'
        )


    def handle(self, *args, **options):
        instances = options['instances']
        if instances:
            for num in range(instances):
                gender = 'M' if num % 2 == 0 else 'F'
                data = generate_user_info_data(gender)
                user_info = UserInfo(**data)
                user_info.save()
                message = f'Added {user_info.username} info to database'
                self.stdout.write(self.style.SUCCESS(message))
