from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Category(models.Model):
    category = models.CharField(max_length=255)
    def __str__(self) -> str:
        return self.category





class Blog(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    time_posted = models.DateTimeField(auto_now_add=timezone.now())
    time_edited = models.DateTimeField(auto_now=timezone.now())
    def __str__(self) -> str:
        return self.title
    def change_time_format(self):
        return f"Job Posted at : {self.time_posted.strftime('%Y-%m-%d')}"
    
