from django.shortcuts import redirect, render, get_object_or_404
import datetime

from apps import stories
from .forms import StoryForm, CommentForm
from django.contrib.auth.decorators import login_required
from .models import Story, Vote, Comment


def frontpage(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    story = Story.objects.filter(created_at__gte=date_from).order_by('-number_of_votes')[0:30]
    template_name = 'story/frontpage.html'
    return render(request, template_name, {'story':story})

def story(request, story_id):
    template_name = 'story/detail.html'
    story = get_object_or_404(Story, pk=story_id)

    if request.method == 'POST':
        form = CommentForm(request.POST)
        
        if form.is_valid():
            comment = form.save(commit=False)
            comment.story = story
            comment.created_by = request.user
            comment.save()
            
            return redirect('story', story_id=story_id)
    else:
        form = CommentForm()
    
    return render(request, template_name, {'story':story,'form':form})

def search(request):
    template_name = 'story/search.html'
    query = request.GET.get('query', '')
    
    if len(query) > 0:
        story = Story.objects.filter(title__icontains=query)
    else:
        story= []
        
    return render(request, template_name, {'story':story, 'query':query})    

def newest(request):
    template_name = 'story/newest.html'
    
    story = Story.objects.all()[0:200]
    
    return render(request, template_name, {'story':story})

@login_required
def vote(request, story_id):
    story = get_object_or_404(Story, pk=story_id)
    
    next_page = request.GET.get('next_page', '')
    
    if story.created_by != request.user and not Vote.objects.filter(created_by=request.user, story=story):
        vote = Vote.objects.create(story=story, created_by=request.user)
        
    if next_page == 'story':
        return redirect('story', story_id=story_id)
    else:
            
        return redirect('frontpage')    
       
@login_required
def submit(request):
    template_name = 'story/submit.html'
    if request.method == 'POST':
        form = StoryForm(request.POST)

        if form.is_valid():
            story = form.save(commit=False)
            story.created_by = request.user
            story.save()
            
            return redirect('frontpage')
    else:        
        form = StoryForm()
        
    return render(request, template_name, {'form': form})