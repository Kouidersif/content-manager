from django.urls import path, include
from .views import (
    ListBlogs,
    CreateBlog,
    RUDObject, 
    UserSignUp
)

urlpatterns = [
    path("", ListBlogs.as_view(), name="listapi"),
    path("post/", CreateBlog.as_view(), name="post_blog"),
    path("blog/<int:pk>/", RUDObject.as_view(), name="rudobj"),
    path("signup/", UserSignUp.as_view(), name="user_signup"),
]
