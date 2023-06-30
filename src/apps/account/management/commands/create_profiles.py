from account.models import Profile, User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Creates profiles for all users who do not have one."

    def handle(self, *args, **options):
        users_without_profile = User.objects.filter(profile=None)

        for user in users_without_profile:
            Profile.objects.create(user=user)
            self.stdout.write(self.style.SUCCESS(f"Profile created for {user.username}"))
