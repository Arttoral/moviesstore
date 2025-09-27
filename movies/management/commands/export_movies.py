from django.core.management.base import BaseCommand
from movies.models import Movie
import json
import os


class Command(BaseCommand):
    help = 'Export movie data to a JSON file'

    def add_arguments(self, parser):
        parser.add_argument(
            '--output',
            type=str,
            default='movies_data.json',
            help='Output file name (default: movies_data.json)'
        )

    def handle(self, *args, **options):
        output_file = options['output']
        
        # Export movie data
        movies_data = []
        for movie in Movie.objects.all():
            movies_data.append({
                'name': movie.name,
                'price': movie.price,
                'description': movie.description,
                'image': str(movie.image) if movie.image else ''
            })

        # Save to JSON file
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(movies_data, f, indent=2, ensure_ascii=False)

        self.stdout.write(
            self.style.SUCCESS(
                f'Successfully exported {len(movies_data)} movies to {output_file}'
            )
        )
        
        # Display exported data
        self.stdout.write('\nExported movies:')
        for movie_data in movies_data:
            self.stdout.write(f'- {movie_data["name"]}: ${movie_data["price"]}')