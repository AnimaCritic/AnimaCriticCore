from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Meta:
    ordering = ("-created",)
class Post(models.Model):
    title = models.CharField(max_length=255)
    summary = RichTextField()
    slug = models.SlugField(max_length=255, unique=True)
    review = models.SmallIntegerField()
    preview = models.ImageField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="blog_post")
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = RichTextUploadingField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:detail", kwargs={"slug": self.slug})
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    body = RichTextField()
    date_added = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['date_added']