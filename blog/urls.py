from django.urls import path, include, re_path
from .views import AddPostView, PostDetailView, PostListView, UpdatePostView
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin

app_name = "blog"

urlpatterns = [
    path("new_post/", AddPostView.as_view(), name="new_post"),
    path("detail/<slug:slug>/", PostDetailView.as_view(), name = "detail"),
    path("", PostListView.as_view(), name="list"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

