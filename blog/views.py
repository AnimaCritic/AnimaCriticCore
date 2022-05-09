from django.shortcuts import render

from django.views.generic import DetailView, ListView, CreateView

from .models import Post

class PostListView(ListView):
    model = Post
    template_name = "blog/post_list.html"
    
class PostDetailView(DetailView):
    model = Post
    template_name = "blog/post_detail.html"
    
class AddPostView(CreateView):
    model = Post
    template_name = "blog/new_post.html"
    fields = ('title', 'summary', 'slug' , 'author' , 'content')
    
def home(request):
    return render(request, 'base.html')