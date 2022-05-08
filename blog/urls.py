from django.urls import path, include, re_path
from .views import AddPostView, PostDetailView, PostListView
from django.conf.urls.static import static
from django.conf import settings

app_name = "blog"

urlpatterns = [
    path("detail/<slug:slug>/", PostDetailView.as_view(), name = "detail"),
    path("", PostListView.as_view(), name="list"),
    path("new_post/", AddPostView.as_view(), name="new_post"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

