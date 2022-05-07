from django.urls import path

from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = "blog"

urlpatterns = [
    path("", views.PostListView.as_view(), name="list"),
    path("<slug:slug>/", views.PostDetailView.as_view(), name = "detail")
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
