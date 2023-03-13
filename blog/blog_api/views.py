from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, AllowAny
from .models import Blog
from .serializer import BlogSerializer,UserSerializer


# Create your views here.


class ListBlogs(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class CreateBlog(generics.CreateAPIView):
    serializer_class = BlogSerializer

class RUDObject(generics.RetrieveUpdateDestroyAPIView):
    permission_classes =  [IsAuthenticatedOrReadOnly]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer



class UserSignUp(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        data = {"message": "User has been successfully created"}
        response.data = data
        return response
    