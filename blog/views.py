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
    
<<<<<<< HEAD
def faq(request):
    return render(request, 'blog/faq.html')

def about_us(request):
    return render(request, 'blog/about_us.html')
=======
def home(request):
    return request("base.html")
>>>>>>> 2be01c53991ae8f66ea453de4f84ea5d7690ab46
