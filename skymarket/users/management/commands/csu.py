from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@admin.ru',
            first_name='Admin',
            last_name='Adminov',
            role='admin',
        )

        user.set_password('123456')
        user.save()
        print('Admin user created.')
