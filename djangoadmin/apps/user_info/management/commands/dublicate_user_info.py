import os

from django.core.management.base import BaseCommand

from djangoadmin.apps.user_info.models import UserInfo
from djangoadmin.apps.user_info.utils import duplicate_model_instance


class Command(BaseCommand):
    help = 'Create duplicates for a UserInfo model entry'

    def add_arguments(self, parser):
        parser.add_argument(
            '--username',
            required=True,
            help='Username to UserInfo instance to duplicate'
        )
        parser.add_argument(
            '--instances',
            required=True,
            type=int,
            help='Number of duplicates to create for a UserInfo instance'
        )


    def handle(self, *args, **options):
        instances = options['instances']
        username = options['username']
        try:
            user_info = UserInfo.objects.get(username=username)
        except UserInfo.DoesNotExist:
            message = f"UserInfo '{username}' doesn't exist"
            self.stdout.write(self.style.ERROR(message))
        for num in range(instances):
            duplicate_model_instance(user_info)
            message = f"Created duplicte for UserInfo '{username}': '{num + 1}'"
            self.stdout.write(self.style.SUCCESS(message))
