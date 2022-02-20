from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User

# Create your views here.

def userprofile(request, username):
    template_name = 'userprofile/userprofile.html'
    user = get_object_or_404(User, username=username)
    
    number_of_votes = 0
    
    for story in user.stories.all():
        number_of_votes = number_of_votes + (story.number_of_votes - 1)
        
    return render(request, template_name, {'user':user, 'number_of_votes':number_of_votes})    

def votes(request, username):
    template_name = 'userprofile/votes.html'
    user = get_object_or_404(User, username=username)
    votes = user.votes.all()
    
    stories = []
    
    for vote in votes:
        stories.append(vote.story)
        
    return render(request, template_name, {'user': user, 'stories':stories})

def submissions(request, username):
    template_name = 'userprofile/submissions.html'
    user = get_object_or_404(User, username=username)
    stories = user.stories.all()
    
    return render(request, template_name, {'user':user, 'stories':stories})