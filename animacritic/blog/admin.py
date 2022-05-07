from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "summary", "slug", "author", "created", "updated")
    prepopulated_fields = {"slug": ("title",)}