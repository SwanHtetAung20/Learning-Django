from django.shortcuts import render

# Create your views here.

def post_list(request):
    print("This is the post_list view")
    return render(request, 'posts/posts_list.html')
