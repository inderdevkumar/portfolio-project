
from django.urls import path, include
from . import views


urlpatterns = [
    
    path('', views.allBlogs, name='allblogs'),
    path('<int:blog_id>', views.detail, name='detail'), # for getting like blog/1 or blog/2 in webpage. make sure to use blog_id in view.py

    
]