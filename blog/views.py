from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
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
    fields = ('title', 'slug', 'summary', 'content')

class UpdatePostView(UpdateView):
    model = Post
    template_name = "blog/update_post.html"
    fields = ('title', 'summary', 'slug', 'content')
    
class DeletePostView(DeleteView):
    model = Post
    template_name = "blog/delete_post.html"
    success_url = reverse_lazy('home')
    
def home(request):
    return request("base.html")