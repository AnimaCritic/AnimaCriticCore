from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

class Meta:
    ordering = ("-created",)
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})