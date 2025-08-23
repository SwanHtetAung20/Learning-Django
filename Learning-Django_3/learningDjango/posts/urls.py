from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('post-new', views.post_new, name="new-post"),
    path("<slug:slug>", views.post_detail, name='detail'),
]

