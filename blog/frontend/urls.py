from django.urls import path
from .views import (
    ListBlogs
)


urlpatterns= [
    path("", ListBlogs.as_view(), name="allblogs"),
]