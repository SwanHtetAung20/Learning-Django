from django.shortcuts import render
from .models import Post
from django.contrib.auth.decorators import login_required


# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {'post': post})

@login_required(login_url='/users/login/')
def post_new(request):
    return render(request, 'posts/post_new.html')
