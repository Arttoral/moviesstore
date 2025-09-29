from django.db import models
from django.contrib.auth.models import User

class MoviePetition(models.Model):
    movie_title = models.CharField(max_length=200)
    movie_description = models.TextField()
    petitioner_name = models.CharField(max_length=100)
    petitioner_email = models.EmailField()
    reason = models.TextField(help_text="Why should this movie be added?")
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"Petition for '{self.movie_title}' by {self.petitioner_name}"
    
    def vote_count(self):
        return self.petitionvote_set.count()
    
    def user_has_voted(self, user):
        if user.is_authenticated:
            return self.petitionvote_set.filter(user=user).exists()
        return False

class PetitionVote(models.Model):
    petition = models.ForeignKey(MoviePetition, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voted_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('petition', 'user')  # Prevents duplicate votes
    
    def __str__(self):
        return f"{self.user.username} voted for '{self.petition.movie_title}'"

