from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import MoviePetition, PetitionVote

def petition_list(request):
    """Display all active petitions"""
    petitions = MoviePetition.objects.filter(is_active=True)
    
    # Add voting status for each petition
    for petition in petitions:
        petition.user_voted = petition.user_has_voted(request.user) if request.user.is_authenticated else False
    
    return render(request, 'petition/petition_list.html', {'petitions': petitions})

def create_petition(request):
    """Handle petition creation"""
    if request.method == 'POST':
        # Create new petition from form data
        petition = MoviePetition.objects.create(
            movie_title=request.POST['movie_title'],
            movie_description=request.POST['movie_description'],
            petitioner_name=request.POST['petitioner_name'],
            petitioner_email=request.POST['petitioner_email'],
            reason=request.POST['reason']
        )
        messages.success(request, 'Petition created successfully!')
        return redirect('petition:list')
    
    return render(request, 'petition/create_petition.html')

@login_required
def vote_petition(request, petition_id):
    """Handle voting on petitions"""
    petition = get_object_or_404(MoviePetition, id=petition_id, is_active=True)
    
    if not petition.user_has_voted(request.user):
        PetitionVote.objects.create(petition=petition, user=request.user)
        messages.success(request, 'Your vote has been recorded!')
    else:
        messages.warning(request, 'You have already voted on this petition.')
    
    return redirect('petition:list')

