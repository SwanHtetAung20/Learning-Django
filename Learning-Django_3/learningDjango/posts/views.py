from django.shortcuts import render
from .models import Post


# Create your views here.

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'posts/posts_list.html', {'posts': posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'posts/post.html', {'post': post})
