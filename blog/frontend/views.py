from django.shortcuts import render
from django.views.generic import ListView
from blog_api.models import Blog
# Create your views here.



class ListBlogs(ListView):
    queryset = Blog.objects.all()
    template_name = "index.html"