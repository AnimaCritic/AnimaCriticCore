"""animacritic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import include, path, re_path

from blog.views import about_us, faq, UpdatePostView, DeletePostView, home, LikeView

urlpatterns = [
    path('', include("blog.urls", namespace="blog")),
    path('accounts/', include('allauth.urls')),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
    path('faq/', faq, name="faq"),
    path('about_us/', about_us, name="about_us"),
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('delete/<int:pk>', DeletePostView.as_view(), name="delete_post"),
    path('like/<int:pk>', LikeView, name="like_post"),
    re_path(r'^ckeditor/', include('ckeditor_uploader.urls')),
]
