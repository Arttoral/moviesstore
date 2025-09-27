from django.core.management.base import BaseCommand
from movies.models import Movie
import os
from django.conf import settings


class Command(BaseCommand):
    help = 'Populate the database with initial movie data'

    def handle(self, *args, **options):
        # Clear existing movies (optional - remove if you want to keep existing data)
        Movie.objects.all().delete()
        self.stdout.write('Cleared existing movie data')

        # Create movie data
        movies_data = [
            {
                'name': 'Inception',
                'price': 15,
                'description': 'Sci-fi masterpiece about dream manipulation and the dangers of imagination.',
                'image': 'movie_images/inception.jpeg'
            },
            {
                'name': 'Avatar',
                'price': 20,
                'description': 'A journey to a distant world and the battle for resources.',
                'image': 'movie_images/avatar.jpg'
            },
            {
                'name': 'The Dark Knight',
                'price': 18,
                'description': 'Gotham\'s vigilante faces the Joker.',
                'image': 'movie_images/DarkKnight.jpeg'
            },
            {
                'name': 'Titanic',
                'price': 12,
                'description': 'A love story set against the backdrop of the sinking Titanic.',
                'image': 'movie_images/Titanic.jpg'
            }
        ]

        created_count = 0
        for movie_data in movies_data:
            movie, created = Movie.objects.get_or_create(
                name=movie_data['name'],
                defaults={
                    'price': movie_data['price'],
                    'description': movie_data['description'],
                    'image': movie_data['image']
                }
            )
            if created:
                created_count += 1
                self.stdout.write(
                    self.style.SUCCESS(f'Created movie: {movie.name}')
                )
            else:
                self.stdout.write(
                    self.style.WARNING(f'Movie already exists: {movie.name}')
                )

        self.stdout.write(
            self.style.SUCCESS(f'Successfully created {created_count} movies')
        )
        
        # Display all movies
        self.stdout.write('\nCurrent movies in database:')
        for movie in Movie.objects.all():
            self.stdout.write(f'- {movie.name}: ${movie.price}')