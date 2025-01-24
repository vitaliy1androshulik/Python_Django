from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    slug = models.SlugField()
    img = models.ImageField(default="default.jpg", blank=True, upload_to='images')
    date = models.DateTimeField(auto_now_add=True)
    created_by =  models.ForeignKey(User, on_delete=models.CASCADE, default=None)
def __str__(self):
        return self.title