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
    
def faq(request):
    return render(request, 'blog/faq.html')

def about_us(request):
    return render(request, 'blog/about_us.html')