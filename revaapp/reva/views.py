from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Post, Club

def home(request):
    posts = Post.objects.all()  # Retrieve all posts
    return render(request, 'home.html', {'posts': posts})

def search(request):
    if 'query' in request.GET:
        query = request.GET['query']
        clubs = Club.objects.filter(name__icontains=query)  # Case-insensitive search for clubs by name
    else:
        clubs = Club.objects.all()
    return render(request, 'search.html', {'clubs': clubs})

@login_required
def create_post(request):
    if request.method == 'POST':
        content = request.POST['content']
        post = Post.objects.create(author=request.user, content=content)
        return redirect('home')
    return render(request, 'create_post.html')

@login_required
def user_profile(request):
    return render(request, 'user_profile.html')

# Other views such as user registration, login, and logout can be handled using Django's built-in views or custom views.

