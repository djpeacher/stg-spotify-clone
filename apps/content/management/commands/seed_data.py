import csv

from django.apps import apps
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.core.management.color import no_style
from django_seed import Seed

User = get_user_model()
Profile = apps.get_model("users", "Profile")
Genre = apps.get_model("music", "Genre")
RecordLabel = apps.get_model("music", "RecordLabel")
Playlist = apps.get_model("music", "Playlist")
Album = apps.get_model("music", "Album")
Artist = apps.get_model("music", "Artist")
Song = apps.get_model("music", "Song")
City = apps.get_model("content", "City")


class Command(BaseCommand):
    """seed_data command"""

    help = "Makes the current database have the same data as the fixture(s), no more, no less."
    args = "fixture [fixture ...]"

    def add_arguments(self, parser):
        super().add_arguments(parser)
        parser.add_argument(
            "--skip-remove",
            action="store_false",
            dest="remove",
            default=True,
            help="Avoid remove any object from db",
        )
        parser.add_argument(
            "--remove-before",
            action="store_true",
            dest="remove_before",
            default=False,
            help="Remove existing objects before inserting and updating new ones",
        )

    def handle(self, *args, **options):
        self.style = no_style()
        try:
            self.seed_data()
        except Exception as exc:
            raise CommandError(exc)

    def seed_data(self):
        # populate city, state data
        with open("setup/cities.csv", newline="") as csvfile:
            rows = csv.reader(csvfile, delimiter=",")
            next(rows)

            city_objs = []
            for row in rows:
                state, name, lat, long = row
                city_objs.append(City(state=state, name=name, latitude=lat, longitude=long))

            City.objects.bulk_create(city_objs, ignore_conflicts=True)

        seeder = Seed.seeder()

        # populate user data
        if not User.objects.filter(username=settings.DJANGO_SUPERUSER_USERNAME).exists():
            User.objects.create_superuser(settings.DJANGO_SUPERUSER_USERNAME, settings.DJANGO_SUPERUSER_EMAIL, settings.DJANGO_SUPERUSER_PASSWORD)

        seeder.add_entity(User, 100)
        seeder.add_entity(Profile, 100)

        # populate artist/song data
        Genre.objects.bulk_create([Genre(name=g) for g in list(dict(Genre.GENRE_CHOICES).keys())], ignore_conflicts=True)

        seeder.add_entity(
            RecordLabel,
            10,
            {
                "name": lambda x: seeder.faker.company(),
            },
        )
        seeder.add_entity(
            Artist,
            200,
            {"name": lambda x: seeder.faker.name()},
        )
        seeder.add_entity(
            Album,
            300,
            {
                "name": lambda x: seeder.faker.sentence(),
            },
        )
        seeder.add_entity(
            Song,
            1000,
            {
                "name": lambda x: seeder.faker.sentence(),
            },
        )
        seeder.add_entity(
            Playlist,
            250,
            {
                "name": lambda x: f"{seeder.faker.name()}'s Playlist",
            },
        )

        seeder.execute()
