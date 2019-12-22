from django.shortcuts import render
from django.shortcuts import get_object_or_404  # for detail function 
from .models import Blog

# Create your views here.
def allBlogs(request):
    blogs= Blog.objects
    return render(request, 'blog/blogs.html', {'Blog_List':blogs})

def detail(request, blog_id):
    detailblog= get_object_or_404(Blog, pk= blog_id)
    return render(request, 'blog/detail.html', {'Blog':detailblog})