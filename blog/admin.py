from django.contrib import admin

# Register your models here.

from .models import Post
from .models import Comment

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("post", "body", "date_added")