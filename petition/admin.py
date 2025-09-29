from django.contrib import admin
from .models import MoviePetition, PetitionVote

class MovieAdmin(admin.ModelAdmin):
    ordering = ['name']
    search_fields = ['name']

@admin.register(MoviePetition)
class MoviePetitionAdmin(admin.ModelAdmin):
    list_display = ['movie_title', 'petitioner_name', 'vote_count', 'created_at', 'is_active']
    list_filter = ['is_active', 'created_at']
    search_fields = ['movie_title', 'petitioner_name']

@admin.register(PetitionVote)
class PetitionVoteAdmin(admin.ModelAdmin):
    list_display = ['petition', 'user', 'voted_at']
    list_filter = ['voted_at']
